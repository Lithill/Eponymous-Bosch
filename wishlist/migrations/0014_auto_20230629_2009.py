# Generated by Django 3.2.19 on 2023-06-29 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0013_wishlist_sale_alert_consent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserWishlist',
        ),
        migrations.DeleteModel(
            name='WaitingList',
        ),
    ]
