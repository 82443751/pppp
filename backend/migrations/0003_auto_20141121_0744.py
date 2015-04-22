# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20141112_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvalUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d', db_index=True)),
                ('sex', models.CharField(db_index=True, max_length=1, verbose_name='\u6027\u522b', choices=[(b'1', '\u7537'), (b'0', '\u5973')])),
                ('age', models.CharField(max_length=4, verbose_name='\u5e74\u9f84')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=20, verbose_name='\u624b\u673a')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Added time')),
            ],
            options={
                'ordering': ['add_time'],
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='useranwser',
            name='user',
            field=models.ForeignKey(to='backend.EvalUser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresult',
            name='user',
            field=models.ForeignKey(to='backend.EvalUser'),
            preserve_default=True,
        ),
    ]
