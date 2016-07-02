# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(max_length=16)),
                ('street', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('country', models.CharField(default=b'United States', max_length=32)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_studio', models.BooleanField(default=False)),
                ('num_bedroom', models.IntegerField()),
                ('num_bathroom', models.IntegerField()),
                ('date_avaialable', models.DateTimeField(auto_now_add=True)),
                ('price_rent', models.FloatField()),
                ('price_buy', models.FloatField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=32)),
                ('is_primary', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='user_profile',
            field=models.ForeignKey(to='zufang.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fang',
            name='user_profile',
            field=models.ManyToManyField(to='zufang.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='fang',
            field=models.ForeignKey(to='zufang.Fang'),
            preserve_default=True,
        ),
    ]
