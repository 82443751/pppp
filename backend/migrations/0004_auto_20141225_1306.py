# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20141225_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userresult',
            old_name='score_explain1',
            new_name='score_explain',
        ),
    ]
