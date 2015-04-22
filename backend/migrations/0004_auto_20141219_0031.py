# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20141121_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultexplain',
            name='question_class',
            field=models.ForeignKey(blank=True, to='backend.QuestionClass', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultexplain',
            name='user_score',
            field=models.IntegerField(db_index=True, null=True, verbose_name='\u7528\u6237\u5f97\u5206', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluser',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='\u90ae\u7bb1'),
            preserve_default=True,
        ),
    ]
