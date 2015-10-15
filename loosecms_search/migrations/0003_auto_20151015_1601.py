# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_search', '0002_auto_20150916_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchmanager',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='searchmanager',
            name='title',
            field=models.CharField(help_text='Give the name of the search manager.', unique=True, max_length=200, verbose_name='title'),
        ),
    ]
