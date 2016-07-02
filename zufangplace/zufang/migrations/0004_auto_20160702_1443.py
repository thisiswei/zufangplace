# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0003_auto_20160702_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='lat',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='lon',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
