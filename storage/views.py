# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import add_message
from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, ListView

from generics.mixins import SearchMixin, QueryMixin
from storage.forms import FileForm
from storage.models import FileModel


class FileListView(SearchMixin, QueryMixin, ListView):
    template_name = "storage/index.html"
    model = FileModel
    context_object_name = "files"

    def get(self, request, *args, **kwargs):
        search_line = request.GET.get('q', None)

        cond = {}
        if search_line:
            cond['file_name__icontains'] = search_line

        self.queryset = self._queryset_filter(**cond)
        return super(FileListView, self).get(redirect, *args, **kwargs)


class FileCreateView(SuccessMessageMixin, CreateView):
    template_name = "storage/upload.html"
    model = FileModel
    form = FileForm
    fields = ["file_name", "notes", "file"]
    success_url = "../"
    success_message = _(u"File \"<a href=\"{href}\">{title}</a>\" uploaded!")

    def get_success_message(self, cleaned_data):
        return self.success_message.format(href=self.object.getUrl(), title=cleaned_data['file_name'])


@csrf_protect
@login_required
def remove(request, file_id):
    if request.user.is_active and request.user.is_staff:
        file = get_object_or_404(FileModel, pk=file_id)
        file.delete()
        add_message(
            request,
            messages.WARNING,
            _("File \"<b>{title}</b>\" is removed!").format(title=file.file_name)
        )
        return redirect("../../")
    else:
        raise Http404


@csrf_protect
@login_required
def download_file(request, file_id):
    if request.user.is_active:
        obj = get_object_or_404(FileModel, pk=file_id)
        obj.count += 1
        obj.save()

        response = HttpResponse(obj.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="%s"' % obj.file.name

        return response
    else:
        raise Http404
