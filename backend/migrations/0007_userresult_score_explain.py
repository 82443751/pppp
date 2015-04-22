# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_userresult_score_explain'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='score_explain',
            field=models.ManyToManyField(to='backend.ResultExplain', through='backend.UserScoreExplain'),
            preserve_default=True,
        ),
    ]
