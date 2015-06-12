# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('deck', models.TextField()),
                ('description', models.TextField()),
                ('released', models.DateTimeField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('deck', models.TextField()),
                ('description', models.TextField()),
                ('released', models.DateTimeField()),
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
    ]
