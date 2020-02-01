# Generated by Django 3.0.2 on 2020-01-30 18:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200130_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 1, 30, 18, 20, 49, 849162, tzinfo=utc)),
        ),
    ]