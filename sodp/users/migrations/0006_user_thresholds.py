# Generated by Django 3.1.12 on 2021-08-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210722_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='thresholds',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
