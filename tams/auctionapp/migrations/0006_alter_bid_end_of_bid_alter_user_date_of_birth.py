# Generated by Django 4.1.2 on 2022-11-26 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='end_of_bid',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
