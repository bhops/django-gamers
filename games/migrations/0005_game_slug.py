# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_remove_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 8, 30, 6, 28, 32, 766927, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
