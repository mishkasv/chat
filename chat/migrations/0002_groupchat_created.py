# Generated by Django 3.2.9 on 2021-11-24 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 24, 10, 35, 33, 137032, tzinfo=utc)),
        ),
    ]
