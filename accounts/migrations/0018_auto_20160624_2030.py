# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_userprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='goalWeight',
            field=models.IntegerField(blank=True, default=160),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.IntegerField(blank=True, default=165),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='startWeight',
            field=models.IntegerField(blank=True, default=180),
        ),
    ]