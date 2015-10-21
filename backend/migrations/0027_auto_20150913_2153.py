# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Added Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='items',
            name='en_content',
            field=models.CharField(help_text='Example: Lower', max_length=300, verbose_name='English'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='items',
            name='score',
            field=models.IntegerField(default=1, help_text='Weight for this option', verbose_name='Weight'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='items',
            name='zh_content',
            field=models.CharField(help_text='Sample: Mild', max_length=300, verbose_name='Chinese'),
            preserve_default=True,
        ),
    ]
