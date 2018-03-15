from django.conf.urls import url
from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostDetailView
from . import views

app_name = BlogConfig.name
urlpatterns = [
    path(r'', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view()),
    path(r'post/upload', views.upload, name='upload'),
]
