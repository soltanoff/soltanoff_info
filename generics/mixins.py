from django.views.generic.base import ContextMixin
from django.views.generic.list import MultipleObjectMixin


class SearchMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(SearchMixin, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q', '')
        return context


class QueryMixin(MultipleObjectMixin):
    # TODO: soltanoff: сделать поиск по нескольким полям в стиле SQL-конструкции `LIKE`
    def _queryset_filter(self, **kwargs):
        if not self.queryset:
            return self.model.objects.filter(**kwargs)
        else:
            return self.queryset.filter(**kwargs)
