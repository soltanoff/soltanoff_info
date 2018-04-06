from django.contrib.auth.decorators import login_required
from django.urls import path

from storage.apps import StorageConfig
from storage.views import FileCreateView, FileListView
from . import views

app_name = StorageConfig.name
urlpatterns = [
    path(r'', login_required(FileListView.as_view()), name='index'),
    path(r'upload/', login_required(FileCreateView.as_view()), name='upload'),
    path(r'remove/<int:file_id>/', views.remove, name='remove'),
    path(r'download_file/<int:file_id>/', views.download_file, name='download_file')
]
