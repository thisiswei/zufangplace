# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('zufang', '0001_initial'), ('zufang', '0002_auto_20160702_1711'), ('zufang', '0003_auto_20160702_2054'), ('zufang', '0004_picture'), ('zufang', '0005_picture_name'), ('zufang', '0006_auto_20160702_2150'), ('zufang', '0007_auto_20160702_2151'), ('zufang', '0008_auto_20160702_2155')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_studio', models.BooleanField(default=False)),
                ('num_bedroom', models.IntegerField(default=None, null=True, blank=True)),
                ('num_bathroom', models.IntegerField()),
                ('date_avaialable', models.DateTimeField(auto_now_add=True)),
                ('price_rent', models.FloatField(default=None, null=True, blank=True)),
                ('price_buy', models.FloatField(default=None, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=32)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fang',
            name='user_profile',
            field=models.ForeignKey(related_name='fangs', to='zufang.UserProfile'),
            preserve_default=True,
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
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.URLField()),
                ('fang', models.ForeignKey(related_name='pictures', to='zufang.Fang')),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
