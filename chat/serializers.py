from rest_framework import serializers
from .models import GroupChat, Messages, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        ordering = ['date_posted']

    user = UserSerializer()
    date_posted = serializers.DateTimeField(format='%x %X')
    date_created = serializers.DateTimeField(format='%x %X')

class GroupChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = ['name', 'users']
    users = serializers.PrimaryKeyRelatedField

class GroupChatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = '__all__'

    group_messages = MessagesSerializer(many=True, read_only=True)
    users = UserSerializer(many=True)

class GroupChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = ['name', 'id', 'created']



class MessagesChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['user','date_posted','text']
        ordering = ['date_posted']

    user = serializers.CharField(source='get_username')
    date_posted = serializers.DateTimeField(format='%x %X')

