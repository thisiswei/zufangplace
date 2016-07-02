# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0005_picture_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
