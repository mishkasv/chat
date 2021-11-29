import functools
import json
import asyncio
import threading
from Test_task_chat.celery import app
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def postpone_massage(room_group, text, anonymous, username):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    channel_layer = get_channel_layer()
    def send(loop):
        import nest_asyncio
        nest_asyncio.apply(loop)
        loop.run_until_complete(channel_layer.group_send(
            room_group,
            {
                'type': 'chat_message',
                'message': text,
                'is_anonymous': anonymous,
                'user': username
            }
        )
        )
    thread = threading.Thread(target=send,args=(loop,))
    thread.start()
    thread.join()


