# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.http import HttpResponseNotFound
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    redirect_url = request.GET.get('next', None)
    error_msg = False

    user = auth.authenticate(username=username, password=password)

    if not redirect_url:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(redirect_url)

    if username and password and user is None:
        error_msg = True

    return render(request, 'account/login.html', {'error': error_msg, 'url': redirect_url})


@csrf_protect
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("../login")
