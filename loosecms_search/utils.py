# -*- coding: utf-8 -*-
from .models import Search


def get_active_models(manager):
    searches = ((search.category, search.title) for search in Search.objects.filter(manager=manager))
    return searches