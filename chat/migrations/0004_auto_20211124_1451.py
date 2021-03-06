# Generated by Django 3.2.9 on 2021-11-24 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_groupchat_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchat',
            name='messages',
            field=models.ForeignKey(default=[], on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='chat.messages'),
        ),
        migrations.AlterField(
            model_name='groupchat',
            name='users',
            field=models.ManyToManyField(default=[], related_name='groups_of_chats', to=settings.AUTH_USER_MODEL),
        ),
    ]
