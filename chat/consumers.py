# chat/consumers.py
import pytz
from django.utils.timezone import datetime
from django.utils import timezone
from django.conf import settings
import json
from .models import Messages, GroupChat
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import postpone_massage

def turn_to_datetime(date_str):
    utc = pytz.timezone(settings.TIME_ZONE)
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
    return utc.localize(date)

@database_sync_to_async
def get_group(name):
    return GroupChat.objects.get(name=name)

@database_sync_to_async
def create_message(user, text, posted_date, group, anonymous):
    if posted_date=='':
        Messages(user=user, text=text, group=group, is_anonymous=anonymous).save()
    else:
        Messages(user=user, text=text, group=group, date_posted=turn_to_datetime(posted_date),
                 is_anonymous=anonymous).save()

def is_delay(delay_date):
    created = timezone.now()
    if delay_date == '':
        posted = created
    else:
        posted = turn_to_datetime(delay_date)
    return posted>created

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.group = await get_group(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        posted_date = text_data_json.get('date_postpone')
        is_anonymous = text_data_json.get('anonymous')
        user = self.scope['user']

        await create_message(user, message, posted_date, self.group, is_anonymous)

        if is_delay(posted_date):
            postpone_massage.apply_async(
                (self.room_group_name, message, is_anonymous, user.username),
                eta=turn_to_datetime(posted_date))
        # Send message to room group
        else:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'is_anonymous': is_anonymous,
                    'user': user.username
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        user = event['user'] if not event['is_anonymous'] else 'Anonymous'
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'date': datetime.now().strftime('%x %X'),
            'user': user
        }))