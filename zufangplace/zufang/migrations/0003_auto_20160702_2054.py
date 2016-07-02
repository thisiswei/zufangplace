# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0002_auto_20160702_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fang',
            name='user_profile',
            field=models.ForeignKey(related_name='fangs', to='zufang.UserProfile'),
            preserve_default=True,
        ),
    ]
