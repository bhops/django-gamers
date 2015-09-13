# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rating',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
