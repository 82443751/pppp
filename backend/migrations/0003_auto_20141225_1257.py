# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_resultexplain_user_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userresult',
            old_name='score_explain',
            new_name='score_explain1',
        ),
    ]
