# Generated by Django 3.2.19 on 2023-06-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='artist',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='dimensions',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='framed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='style',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
