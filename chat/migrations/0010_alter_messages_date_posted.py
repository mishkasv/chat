# Generated by Django 3.2.9 on 2021-11-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_alter_messages_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date_posted',
            field=models.DateTimeField(),
        ),
    ]
