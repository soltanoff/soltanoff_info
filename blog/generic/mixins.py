from django.views.generic.base import ContextMixin

from blog.models import TagModel


class TagMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = TagModel.objects.all()
        if hasattr(self, 'request'):
            tag_id = self.request.GET.get('tag', None)
            context['current_tags'] = TagModel.objects.get(pk=tag_id) if tag_id else None
        return context
