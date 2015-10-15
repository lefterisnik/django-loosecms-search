# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

from haystack.forms import SearchForm

from .models import *
from .utils import get_active_models


class LoosecmsSearchForm(SearchForm):
    def __init__(self, *args, **kwargs):
        self.manager = kwargs.pop('manager', None)

        super(LoosecmsSearchForm, self).__init__(*args, **kwargs)

        self.fields['q'] = forms.CharField(required=False,
                                           widget=forms.TextInput(attrs={
                                               'class': 'form-control',
                                               'type': 'search',
                                               'placeholder': 'Αναζήτηση'}))
        self.fields['start_date'] = forms.DateField(required=False,
                                                    widget=forms.DateInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': 'Από'}))
        self.fields['end_date'] = forms.DateField(required=False,
                                                  widget=forms.DateInput(attrs={
                                                      'class': 'form-control',
                                                      'placeholder': 'Μέχρι'}))
        self.fields['models'] = forms.MultipleChoiceField(required=False,
                                                          choices=get_active_models(self.manager),
                                                          widget=forms.CheckboxSelectMultiple)

    def get_models(self):
        """Return an alphabetical list of model classes in the index."""
        search_models = []

        if self.is_valid():
            for model in self.cleaned_data['models']:
                search_models.append(models.get_model(*model.split('.')))

        return search_models

    def get_user_models(self):
        search_models = []

        for model in get_active_models(self.manager):
            search_models.append(models.get_model(*model[0].split('.')))

        return search_models

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(LoosecmsSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        # Check to see if a start_date was chosen.
        if self.cleaned_data['start_date']:
            #print self.cleaned_data['start_date']
            sqs = sqs.filter(ctime__gte=self.cleaned_data['start_date'])

        # Check to see if an end_date was chosen.
        if self.cleaned_data['end_date']:
            #print self.cleaned_data['end_date']
            sqs = sqs.filter(ctime__lte=self.cleaned_data['end_date'])

        # Check to see if an model was chosen.
        if self.cleaned_data['models']:
            sqs = sqs.models(*self.get_models())
        else:
            sqs = sqs.models(*self.get_user_models())

        return sqs

