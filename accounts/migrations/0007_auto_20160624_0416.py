# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 04:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20160624_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True, default=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='goalWeight',
            field=models.IntegerField(blank=True, default=160),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='height',
            field=models.IntegerField(blank=True, default=165),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='startDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='startWeight',
            field=models.IntegerField(blank=True, default=180),
        ),
    ]
