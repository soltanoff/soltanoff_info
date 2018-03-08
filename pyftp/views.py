# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

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


@csrf_protect
@login_required
def upload(request):
    file = request.FILES.get('file', None)
    file_name = request.POST.get('file_name', '')
    notes = request.POST.get('notes', '')

    if file and file_name and notes:
        file_model = FileModel(file_name=file_name, notes=notes, file=file)
        file_model.save()

        request.file_uploaded = [file_model.id, file_model.file_name]
        return index(request)

    return render(
        request,
        'pyftp/upload.html',
        {
            'errors': bool(file_name or notes or file),
            'file': file,
            'file_name': file_name,
            'notes': notes
        }
    )


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
