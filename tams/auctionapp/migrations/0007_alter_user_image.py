# Generated by Django 4.1.2 on 2022-11-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0006_alter_bid_end_of_bid_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='display-photos/default-dp.png', upload_to='display-photos/%Y/%m/%D/'),
        ),
    ]
