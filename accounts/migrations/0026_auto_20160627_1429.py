# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20160627_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='hobbies',
            field=models.TextField(blank=True, default=b'Running'),
        ),
    ]
