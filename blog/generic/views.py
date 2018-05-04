from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import ModelFormMixin

from blog.forms import PostForm
from blog.models import PostModel


class BasePostView(SuccessMessageMixin, ModelFormMixin):
    model = PostModel
    form = PostForm
    fields = ["title", "tags", "entry", "content"]

    def get_success_message(self, cleaned_data):
        return self.success_message.format(href=self.object.get_url(), title=cleaned_data['title'])

    def get_success_url(self):
        return self.object.get_url()
