# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from pyftp.models import FileModel


# TODO: blog logic + comment + pages + ajax + picture
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
