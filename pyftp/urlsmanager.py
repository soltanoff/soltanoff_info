from django.urls import path

from . import views

app_name = 'pyftp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'upload/', views.upload, name='upload'),
    path(r'remove/<int:file_id>/', views.remove, name='remove'),
    path(r'download_file/<int:file_id>[0-9]/', views.download_file, name='download_file')
]
