# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='deck',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='deck',
        ),
        migrations.AlterField(
            model_name='game',
            name='added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='released',
            field=models.DateField(auto_now_add=True),
        ),
    ]
