# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20160624_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='full_name',
            field=models.CharField(blank=True, default=b'Alex Smith', max_length=120),
        ),
    ]
