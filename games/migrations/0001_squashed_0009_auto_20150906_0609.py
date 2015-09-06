# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('games', '0001_initial'), ('games', '0002_game_slug'), ('games', '0003_auto_20150830_0559'), ('games', '0004_remove_game_slug'), ('games', '0005_game_slug'), ('games', '0006_auto_20150830_0652'), ('games', '0007_platform_slug'), ('games', '0008_auto_20150905_1845'), ('games', '0009_auto_20150906_0609')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('released', models.DateTimeField()),
                ('added', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='pc', unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(related_name='games', to='games.Platform'),
        ),
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='released',
            field=models.DateField(auto_now_add=True),
        ),
    ]
