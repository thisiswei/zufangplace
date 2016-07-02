# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0007_auto_20160702_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='url',
            new_name='source',
        ),
    ]
