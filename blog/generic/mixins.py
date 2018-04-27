from django.core.paginator import InvalidPage
from django.http import Http404
from django.utils.translation import gettext as _
from django.views.generic.base import ContextMixin
from django.views.generic.list import MultipleObjectMixin

from blog.models import TagModel


class TagMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = TagModel.objects.all()
        if hasattr(self, 'request'):
            tag_id = self.request.GET.get('tag', None)
            context['current_tags'] = TagModel.objects.get(pk=tag_id) if tag_id else None
        return context


class PageMixin(MultipleObjectMixin):
    allow_empty = True
    paginate_by = 2
    paginate_orphans = 2
    page_kwarg = "p"
    page_numbers_count = 5

    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)

        first_page = self.page_numbers_count * int(context['page_obj'].number / self.page_numbers_count)
        count = self.page_numbers_count + first_page

        if first_page >= context['page_obj'].paginator.num_pages:
            first_page = context['page_obj'].paginator.num_pages - self.page_numbers_count
        elif first_page == 0:
            first_page = 1

        context['page_range'] = range(
            first_page,
            (count if count < context['page_obj'].paginator.num_pages else context['page_obj'].paginator.num_pages) + 1
        )
        return context

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(
            queryset,
            page_size,
            orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty()
        )

        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1

        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number if page_number <= paginator.num_pages else paginator.num_pages)
        except InvalidPage as e:
            raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
                'page_number': page_number,
                'message': str(e)
            })
        finally:
            return paginator, page, page.object_list, page.has_other_pages()
