# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from haystack.forms import model_choices

from loosecms.models import Plugin


class SearchManager(Plugin):
    default_type = 'SearchManagerPlugin'

    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give the name of the search manager/'))
    ctime = models.DateTimeField(editable=False, default=timezone.now)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


class Search(models.Model):
    choices = model_choices()

    title = models.CharField(_('title'), max_length=100,
                             help_text=_('Give the name of search box.'))
    category = models.CharField(_('category'), max_length=50, choices=choices,
                                help_text=_('Select the model for searching.'))
    manager = models.ForeignKey(SearchManager)

    def __unicode__(self):
        return self.title
