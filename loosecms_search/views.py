from haystack.views import SearchView


class LoosecmsSearchView(SearchView):

    def __init__(self, manager, *args, **kwargs):
        self.manager = manager
        super(LoosecmsSearchView, self).__init__(*args, **kwargs)

    def build_form(self, form_kwargs=None):
        kwargs = {
            'manager': self.manager,
        }

        if form_kwargs:
            kwargs.update(form_kwargs)

        return super(LoosecmsSearchView, self).build_form(kwargs)