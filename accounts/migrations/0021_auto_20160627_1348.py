# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 13:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20160626_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='goalDate',
            field=models.DateField(default=datetime.date(2016, 7, 9)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='startDate',
            field=models.DateField(default=datetime.date(2016, 6, 27)),
        ),
    ]
