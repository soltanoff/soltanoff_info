from django.db.models import Q
from django.views.generic.base import ContextMixin
from django.views.generic.list import MultipleObjectMixin
from functools import reduce


class SearchMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(SearchMixin, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q', '')
        return context


# TODO: need to analyze the standart Django ORM 
class QueryMixin(MultipleObjectMixin):
    def _queryset_filter(self, *args, **kwargs):
        if not self.queryset:
            return self.model.objects.filter(self._join_and(*args, **kwargs))
        else:
            return self.queryset.filter(self._join_and(*args, **kwargs))

    def _join_or(self, *args, **kwargs):
        result = []
        if args:
            result.append(reduce(lambda x, y: Q(x) | Q(y), args))
        if kwargs and len(kwargs.keys()) > 1:
            result.append(reduce(lambda x, y: Q(**{x: kwargs[x]} if x in kwargs else x) | Q(**{y: kwargs[y]}), kwargs))
        else:
            result.append(Q(**kwargs))
        return reduce(lambda x, y: Q(x) | Q(y), filter(bool, result), Q())

    def _join_and(self, *args, **kwargs):
        result = []
        if args:
            result.append(reduce(lambda x, y: Q(x) & Q(y), args))
        if kwargs and len(kwargs.keys()) > 1:
            result.append(reduce(lambda x, y: Q(**{x: kwargs[x]} if x in kwargs else x) & Q(**{y: kwargs[y]}), kwargs))
        else:
            result.append(Q(**kwargs))
        return reduce(lambda x, y: Q(x) & Q(y), filter(bool, result), Q())
