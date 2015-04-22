# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20150105_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='our_trade_no',
            field=models.CharField(default=b'', max_length=50, null=True, verbose_name='\u8ba2\u5355\u53f7', blank=True),
            preserve_default=True,
        ),
    ]
