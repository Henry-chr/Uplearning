# Generated by Django 3.1 on 2020-08-26 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_pp_autologon_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='pp_autologon_test',
            name='insert_time',
            field=models.TimeField(default=datetime.datetime(2020, 8, 26, 18, 7, 37, 11700)),
        ),
    ]