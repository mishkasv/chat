# Generated by Django 3.2.9 on 2021-11-25 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_alter_messages_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
