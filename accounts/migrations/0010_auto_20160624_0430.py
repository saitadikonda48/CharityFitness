# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 04:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20160624_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='goalDate',
            field=models.DateField(default=datetime.datetime(2016, 7, 6, 4, 30, 11, 558533, tzinfo=utc)),
        ),
    ]
