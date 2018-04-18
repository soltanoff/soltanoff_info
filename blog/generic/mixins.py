from django.views.generic.base import ContextMixin

from blog.models import TagModel


class TagMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = TagModel.objects.all()
        return context
