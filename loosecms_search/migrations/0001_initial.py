# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Give the name of search box.', max_length=100, verbose_name='title')),
                ('category', models.CharField(help_text='Select the model for searching.', max_length=50, verbose_name='category', choices=[('loosecms_article.article', 'Articles'), ('loosecms_doc.doc', 'Docs')])),
            ],
        ),
        migrations.CreateModel(
            name='SearchManager',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text='Give the name of the search manager/', max_length=200, verbose_name='title')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            bases=('loosecms.plugin',),
        ),
        migrations.AddField(
            model_name='search',
            name='manager',
            field=models.ForeignKey(to='loosecms_search.SearchManager'),
        ),
    ]
