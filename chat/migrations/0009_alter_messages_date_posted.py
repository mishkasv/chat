# Generated by Django 3.2.9 on 2021-11-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20211125_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
