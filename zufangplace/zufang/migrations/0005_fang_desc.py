# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0004_auto_20160703_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='fang',
            name='desc',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]