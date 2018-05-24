# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from account.apps import AccountConfig


class CustomLoginView(LoginView):
    template_name = "account/login.html"
    redirect_authenticated_user = True

    def get_redirect_url(self):
        redirect_to = super(CustomLoginView, self).get_redirect_url()
        return redirect_to if redirect_to else AccountConfig.default_redirect_url


# TODO: soltanoff: add logout page + view
@csrf_protect
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(AccountConfig.default_redirect_url)
