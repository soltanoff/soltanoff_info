from django.conf.urls import url

from . import views

app_name = 'pyftp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^remove/(?P<file_id>[0-9]+)/$', views.remove, name='remove'),
    url(r'^download_file/(?P<file_id>[0-9]+)/$', views.download_file, name='download_file')
]
