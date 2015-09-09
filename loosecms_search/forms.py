# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from haystack.forms import SearchForm
from .models import *


class TsSearchForm(SearchForm):
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'search', 'placeholder': 'Αναζήτηση'}))
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Από'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Μέχρι'}))
    ts_models = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)

    def get_models(self):
        """Return an alphabetical list of model classes in the index."""
        search_models = []

        if self.is_valid():
            for model in self.cleaned_data['ts_models']:
                search_models.append(models.get_model(*model.split('.')))

        return search_models

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(TsSearchForm, self).search()

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
        # TODO: Check which model is active
        if self.cleaned_data['ts_models']:
            sqs = sqs.models(*self.get_models())

        return sqs

