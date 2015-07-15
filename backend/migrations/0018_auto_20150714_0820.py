# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20150712_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscoreexplain',
            name='question_class',
            field=models.ForeignKey(blank=True, to='backend.QuestionClass', null=True),
        ),
        migrations.AlterField(
            model_name='userresult',
            name='score_explain',
            field=models.ManyToManyField(to='backend.ResultExplain', null=True, through='backend.UserScoreExplain', blank=True),
        ),
    ]
