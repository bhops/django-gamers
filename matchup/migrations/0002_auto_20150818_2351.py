# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchup', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Matchup',
            new_name='LookingForPost',
        ),
        migrations.AlterModelOptions(
            name='lookingforpost',
            options={'ordering': ('user',)},
        ),
    ]
