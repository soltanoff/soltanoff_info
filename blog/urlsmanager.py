from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostDetailView, PostListView, PostCreateView

app_name = BlogConfig.name
urlpatterns = [
    path(r'', PostListView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
    path(r'post/upload', login_required(PostCreateView.as_view()), name='upload'),
]
