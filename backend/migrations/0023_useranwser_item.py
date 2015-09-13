# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_auto_20150830_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranwser',
            name='item',
            field=models.ForeignKey(blank=True, to='backend.Items', null=True),
        ),
    ]
