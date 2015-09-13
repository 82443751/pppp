# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_auto_20150719_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zh_content', models.CharField(help_text='\u793a\u4f8b\uff1a\u8f7b\u5fae', max_length=300, verbose_name='\u4e2d\u6587')),
                ('en_content', models.CharField(help_text='Example: Lower', max_length=300, verbose_name='\u82f1\u6587')),
                ('score', models.IntegerField(default=1, help_text='\u8be5\u9009\u9879\u7684\u5206\u503c', verbose_name='\u5206\u503c')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['add_time'],
                'verbose_name': '\u95ee\u9898\u884c\u53ef\u9009\u9879',
                'verbose_name_plural': '\u95ee\u9898\u884c\u53ef\u9009\u9879',
            },
        ),
        migrations.AlterField(
            model_name='resultexplain',
            name='is_show_simple_content',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u5728\u7b80\u8981\u7ed3\u679c\u4e2d\u663e\u793a'),
        ),
        migrations.AddField(
            model_name='question',
            name='items',
            field=models.ManyToManyField(to='backend.Items'),
        ),
    ]
