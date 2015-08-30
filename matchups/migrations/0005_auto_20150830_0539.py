# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchups', '0004_auto_20150825_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lookingforpost',
            name='game',
            field=models.ForeignKey(to='games.Game'),
        ),
    ]
