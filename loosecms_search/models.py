# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from haystack.forms import model_choices

from loosecms.models import Plugin


class SearchManager(Plugin):
    default_type = 'SearchManagerPlugin'

    title = models.CharField(_('title'), max_length=200, unique=True,
                             help_text=_('Give the name of the search manager.'))
    ctime = models.DateTimeField(auto_now_add=True)

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

    def clean(self):
        """
        Don't allow other search with the same searchmanager has the same category
        :return:
        """
        searches_category = Search.objects.filter(manager=self.manager, category=self.category).exclude(pk=self.pk)
        searches_title = Search.objects.filter(manager=self.manager, title=self.title).exclude(pk=self.pk)
        if searches_category.count() != 0:
            msg = _('In this manager is already exist this category.')
            raise ValidationError({'category': msg})

        if searches_title.count() != 0:
            msg = _('In this manager is already exist this title.')
            raise ValidationError({'title': msg})

    def __unicode__(self):
        return self.title

