from haystack.views import SearchView

class TsSearchView(SearchView):

    def build_form(self, form_kwargs=None):
        form = super(TsSearchView, self).build_form(form_kwargs)
        form.fields['ts_models'].choices = self.choices

        return form

    def set_choices(self, choices):
        self.choices = choices