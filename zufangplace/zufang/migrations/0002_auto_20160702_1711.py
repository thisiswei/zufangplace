# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='fang',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='fang',
            name='city',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fang',
            name='country',
            field=models.CharField(default=b'United States', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fang',
            name='lat',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fang',
            name='lon',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fang',
            name='state',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fang',
            name='street',
            field=models.CharField(max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fang',
            name='zipcode',
            field=models.CharField(default=10021, max_length=16),
            preserve_default=False,
        ),
    ]
