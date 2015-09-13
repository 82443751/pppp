# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_useranwser_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscoreexplain',
            name='item',
            field=models.ForeignKey(blank=True, to='backend.Items', null=True),
        ),
    ]
