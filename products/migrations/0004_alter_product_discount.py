# Generated by Django 3.2.19 on 2023-06-21 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230621_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(95), django.core.validators.MinValueValidator(0)]),
        ),
    ]
