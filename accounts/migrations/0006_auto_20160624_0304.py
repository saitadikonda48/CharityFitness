# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 03:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160624_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='bio',
            new_name='hobbies',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_member',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twitter_handle',
        ),
    ]
