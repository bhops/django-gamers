# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchup', '0002_auto_20150818_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lookingforpost',
            name='game',
            field=models.ForeignKey(to='games.OwnedGame'),
        ),
    ]
