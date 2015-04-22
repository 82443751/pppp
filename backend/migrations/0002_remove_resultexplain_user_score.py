# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_squashed_0007_userresult_score_explain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultexplain',
            name='user_score',
        ),
    ]
