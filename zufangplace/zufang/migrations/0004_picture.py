# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0003_auto_20160702_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('fang', models.ForeignKey(related_name='pictures', to='zufang.Fang')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
