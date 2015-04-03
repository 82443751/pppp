# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_class',
            field=models.ForeignKey(blank=True, to='backend.QuestionClass', null=True),
            preserve_default=True,
        ),
    ]
