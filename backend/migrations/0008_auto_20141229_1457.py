# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20141225_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='pay_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Added time', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userresult',
            name='trade_no',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u652f\u4ed8\u5b9d\u8ba2\u5355\u53f7', blank=True),
            preserve_default=True,
        ),
    ]
