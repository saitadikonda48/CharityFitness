# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 19:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160623_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=320, null=True, verbose_name=b'Face profile url')),
                ('twitter_handle', models.CharField(blank=True, max_length=320, null=True, verbose_name=b'Twitter handle')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
