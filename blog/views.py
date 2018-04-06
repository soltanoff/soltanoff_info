# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import add_message
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin

from blog.forms import PostForm
from blog.models import PostModel


# TODO: soltanoff: use the thumbnails for article, add new field to the PostModel: `icon`


class PostDetailView(DetailView):
    template_name = "blog/post.html"
    model = PostModel
    context_object_name = "post"
    slug_field = "title"


class PostListView(ListView):
    template_name = "blog/index.html"
    model = PostModel
    queryset = PostModel.objects.all()
    context_object_name = "posts"
    allow_empty = True
    paginate_orphans = 10
    page_kwarg = "p"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q', '')

        if context['search']:
            # TODO: сделать поиск по нескольким полям в стиле SQL-конструкции `LIKE`
            self.queryset = PostModel.objects.filter(title__icontains=context['search'])
        else:
            self.queryset = PostModel.objects.all()
        context[self.context_object_name] = self.queryset
        return context


class BasePostView(SuccessMessageMixin, ModelFormMixin):
    model = PostModel
    form = None
    fields = ["title", "entry", "content"]

    def get_success_message(self, cleaned_data):
        return self.success_message.format(href=self.object.getUrl(), title=cleaned_data['title'])

    def get_success_url(self):
        return self.object.getUrl()


class PostCreateView(BasePostView, CreateView):
    template_name = "blog/upload.html"
    success_message = _(u"Article \"<a href=\"{href}\">{title}</a>\" created!")

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def get(self, request, *args, **kwargs):
        self.form = PostForm()
        return super(PostCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = PostForm(request.POST)
        return super(PostCreateView, self).post(request, *args, **kwargs)


class PostUpdateView(BasePostView, UpdateView):
    template_name = "blog/update.html"
    success_message = _(u"Article \"<a href=\"{href}\">{title}</a>\" updated!")


@csrf_protect
@login_required
def remove(request, post_id):
    if request.user.is_active and request.user.is_staff:
        post = PostModel.objects.get(id=post_id)
        post.delete()
        add_message(
            request,
            messages.WARNING,
            _("Post \"<b>{title}</b>\" is removed!").format(title=post.title)
        )
        return redirect("/")
    else:
        raise Http404
