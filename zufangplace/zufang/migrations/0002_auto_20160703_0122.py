# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0001_squashed_0008_auto_20160702_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fang',
            old_name='date_avaialable',
            new_name='date_available',
        ),
    ]
