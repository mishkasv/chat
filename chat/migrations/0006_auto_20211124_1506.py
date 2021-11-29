# Generated by Django 3.2.9 on 2021-11-24 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20211124_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupchat',
            name='messages',
        ),
        migrations.AddField(
            model_name='messages',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='masseges', to='chat.groupchat'),
        ),
    ]
