from django.urls import path

from blog.apps import BlogConfig
from . import views

app_name = BlogConfig.name
urlpatterns = [
    path(r'', views.index, name='index'),
]
