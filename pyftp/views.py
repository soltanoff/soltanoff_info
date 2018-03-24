# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView

from pyftp.forms import FileForm
from pyftp.models import FileModel


# TODO: soltanoff: use AJAX  https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
# TODO: view
@csrf_protect
@login_required
def index(request):
    search_param = request.GET.get('q', '')
    if search_param:
        files = FileModel.objects.filter(file_name__contains=search_param)
    else:
        files = FileModel.objects.all()

    add_file_param = request.GET.get('add', '')
    if add_file_param:
        file = FileModel.objects.get(pk=add_file_param)
        if file:
            request.file_uploaded = [file.id, file.file_name]

    return render(
        request,
        'pyftp/index.html',
        {
            'files': files,
            'search': search_param,
            'file_removed': request.file_removed if hasattr(request, 'file_removed') else '',
            'file_uploaded': request.file_uploaded if hasattr(request, 'file_uploaded') else []
        }
    )


class FileCreateView(CreateView):
    template_name = "pyftp/upload.html"
    model = FileModel
    form = None
    fields = ["file_name", "notes", "file"]
    success_url = "../"

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
        return HttpResponseRedirect(self.get_success_url() + '?add=%s' % self.object.pk)


@csrf_protect
@login_required
def remove(request, file_id):
    if request.user.is_active and request.user.is_staff:
        file_model = FileModel.objects.filter(id=file_id)
        if len(file_model):
            request.file_removed = "%s (%s)" % (file_model[0].file_name, file_model[0].file.name)

        file_model.delete()
        return index(request)
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
