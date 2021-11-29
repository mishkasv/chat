from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime

class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('user_messages', 'groups_of_chats')

class GroupChatManager(models.Manager):
    def get_gueryset(self):
        return super().get_queryset().prefetch_related('group_messages__user', 'group_messages', 'users', 'users__user_messages')

class MessagesManager(models.Manager):
    def get_gueryset(self):
        return super().get_queryset().prefetch_related('user','group')

class User(AbstractUser):
    objects = CustomUserManager()
    email = None

class GroupChat(models.Model):
    objects = GroupChatManager()

    name = models.CharField(max_length=70,unique=True,null=False)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    users = models.ManyToManyField('User',related_name='groups_of_chats')

    def __str__(self):
        return self.name

class Messages(models.Model):
    objects = MessagesManager()

    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='user_messages')
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now,blank=True)
    text = models.TextField()
    group = models.ForeignKey('GroupChat', on_delete=models.CASCADE, related_name='group_messages', default=None)
    is_anonymous = models.BooleanField(default=False)

    @property
    def is_posted(self):
        return datetime.now() >= self.date_posted

    def __str__(self):
        return 'message'+self.user.username

    def get_username(self):
        if self.is_anonymous:
            return 'Anonymous'
        return self.user.username


# Create your models here.
