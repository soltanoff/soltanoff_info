# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import add_message
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, ListView
from django.utils.translation import gettext as _

from storage.forms import FileForm
from storage.models import FileModel


# TODO: soltanoff: use AJAX https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
class FileListView(ListView):
    template_name = "storage/index.html"
    model = FileModel
    queryset = FileModel.objects.all()
    context_object_name = "files"

    def get_context_data(self, **kwargs):
        context = super(FileListView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q', '')

        if context['search']:
            self.queryset = FileModel.objects.filter(file_name__icontains=context['search'])
        else:
            self.queryset = FileModel.objects.all()
        context[self.context_object_name] = self.queryset
        return context


class FileCreateView(SuccessMessageMixin, CreateView):
    template_name = "storage/upload.html"
    model = FileModel
    form = None
    fields = ["file_name", "notes", "file"]
    success_url = "../"
    success_message = _(u"File \"<a href=\"{href}\">{title}</a>\" uploaded!")

    # TODO: soltanoff: need to fix this
    def get_success_message(self, cleaned_data):
        # file = FileModel.objects.get(**cleaned_data)
        return self.success_message.format(href=self.object.getUrl(), title=cleaned_data['file_name'])

    def get_context_data(self, **kwargs):
        context = super(FileCreateView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def get(self, request, *args, **kwargs):
        self.form = FileForm()
        return super(FileCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = FileForm(request.POST)
        return super(FileCreateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super(FileCreateView, self).form_valid(form)

@csrf_protect
@login_required
def remove(request, file_id):
    if request.user.is_active and request.user.is_staff:
        file = FileModel.objects.get(id=file_id)
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
