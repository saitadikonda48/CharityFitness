# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 04:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile_goaldate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='goalDate',
            field=models.DateField(default=datetime.datetime(2016, 8, 23, 4, 28, 7, 431422, tzinfo=utc)),
        ),
    ]
