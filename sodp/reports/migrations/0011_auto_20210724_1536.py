# Generated by Django 3.1.12 on 2021-07-24 15:36

from django.db import migrations, models
from datetime import timezone
import datetime



class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20210723_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='errorDescription',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='error description'),
        ),
        migrations.AddField(
            model_name='report',
            name='numRetries',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='processingEndDate',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 1, 7, 15, 12, 655838)),
        ),
            #preserve_default=False,
        migrations.AddField(
            model_name='report',
            name='processingStartDate',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 1, 7, 15, 12, 655838)),
        ),
    ]
