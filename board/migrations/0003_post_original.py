# Generated by Django 3.2.8 on 2021-12-01 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20211027_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='original',
            field=models.BooleanField(default=False),
        ),
    ]
