# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LooseCMSSearchConfig(AppConfig):
    name = 'loosecms_search'
    verbose_name = _('Loose CMS Plugin - Search')