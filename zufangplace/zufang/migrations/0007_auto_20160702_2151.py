# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0006_auto_20160702_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
