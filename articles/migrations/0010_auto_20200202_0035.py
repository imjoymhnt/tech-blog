# Generated by Django 3.0.2 on 2020-02-01 19:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200201_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 2, 1, 19, 5, 45, 973993, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
