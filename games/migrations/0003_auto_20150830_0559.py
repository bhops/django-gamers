# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
