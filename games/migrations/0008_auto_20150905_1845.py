# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_platform_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='company',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='description',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='released',
        ),
        migrations.AlterField(
            model_name='game',
            name='released',
            field=models.DateField(auto_now_add=True),
        ),
    ]
