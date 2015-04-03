# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_userresult_our_trade_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userscoreexplain',
            options={'ordering': ['add_time'], 'verbose_name': '\u7528\u6237\u7684\u5f97\u5206\u8bf4\u660e', 'verbose_name_plural': '\u7528\u6237\u7684\u5f97\u5206\u8bf4\u660e'},
        ),
        migrations.AddField(
            model_name='useranwser',
            name='user_result',
            field=models.ForeignKey(blank=True, to='backend.UserResult', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='explain',
            field=models.ManyToManyField(to='backend.ResultExplain', verbose_name='Result Explain'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.ManyToManyField(to='backend.Question', verbose_name='Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='our_trade_no',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name='order no.', blank=True),
            preserve_default=True,
        ),
    ]
