# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20160624_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, default=b'Alex Smith', max_length=120),
        ),
    ]