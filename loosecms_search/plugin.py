# -*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _


from .views import TsSearchView
from .forms import *
from .models import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class SearchInline(admin.StackedInline):
    model = Search
    extra = 1


class SearchManagerPlugin(PluginModelAdmin):
    model = SearchManager
    name = _('Search')
    template = "plugin/search.html"
    plugin = True
    inlines = [
        SearchInline,
    ]

    def render(self, context, manager):
        searches = ((search.category, search.title) for search in Search.objects.filter(manager=manager))
        searchview = TsSearchView(template=self.template, form_class=TsSearchForm)
        searchview.set_choices(searches)
        return HttpResponse(searchview.__call__(context['request'])).content

plugin_pool.register_plugin(SearchManagerPlugin)