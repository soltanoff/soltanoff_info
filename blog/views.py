# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from pyftp.models import FileModel


@csrf_protect
def index(request):
    search_param = request.GET.get('q', '')
    if search_param:
        files = FileModel.objects.filter(file_name__contains=search_param)
    else:
        files = FileModel.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'files': files,
            'search': search_param,
            'file_removed': request.file_removed if hasattr(request, 'file_removed') else '',
            'file_uploaded': request.file_uploaded if hasattr(request, 'file_uploaded') else []
        }
    )
