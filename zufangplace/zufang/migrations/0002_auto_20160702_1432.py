# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fang',
            name='num_bedroom',
            field=models.IntegerField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fang',
            name='price_buy',
            field=models.FloatField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fang',
            name='price_rent',
            field=models.FloatField(default=None, null=True),
            preserve_default=True,
        ),
    ]
