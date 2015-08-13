# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import SearchManager, Search
from .plugin import SearchPlugin

admin.site.register(SearchManager, SearchPlugin)
admin.site.register(Search)