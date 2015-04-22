# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20141220_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresult',
            name='score_explain',
        ),
    ]
