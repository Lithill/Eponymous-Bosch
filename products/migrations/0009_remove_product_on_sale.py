# Generated by Django 3.2.19 on 2023-06-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_on_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='on_sale',
        ),
    ]
