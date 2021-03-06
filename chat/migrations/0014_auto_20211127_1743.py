# Generated by Django 3.2.9 on 2021-11-27 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_alter_messages_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='group_messages', to='chat.groupchat'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
