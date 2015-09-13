# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_userscoreexplain_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscoreexplain',
            name='explain',
            field=models.ForeignKey(blank=True, to='backend.ResultExplain', null=True),
        ),
    ]
