# Generated by Django 3.0.2 on 2020-01-31 19:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200201_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 1, 31, 19, 18, 59, 917644, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.CharField(default='', max_length=250),
        ),
    ]
