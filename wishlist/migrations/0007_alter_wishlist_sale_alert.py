# Generated by Django 3.2.19 on 2023-06-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0006_alter_wishlist_sale_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='sale_alert',
            field=models.BooleanField(default=False, verbose_name='Wants alert'),
        ),
    ]
