# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='category',
            field=models.CharField(help_text='Select the model for searching.', max_length=50, verbose_name='category', choices=[('loosecms_article.article', 'Articles'), ('loosecms_doc.doc', 'Documents')]),
        ),
    ]
