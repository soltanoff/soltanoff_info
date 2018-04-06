from django.contrib.auth.decorators import login_required
from django.urls import path

from blog import views
from blog.apps import BlogConfig
from blog.views import PostDetailView, PostListView, PostCreateView, PostUpdateView

app_name = BlogConfig.name
urlpatterns = [
    path(r'', PostListView.as_view(), name='index'),
    path(r'post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path(r'post/upload/', login_required(PostCreateView.as_view()), name='upload'),
    path(r'post/remove/<int:post_id>/', login_required(views.remove), name='remove'),
    path(r'post/update/<int:pk>/', login_required(PostUpdateView.as_view()), name='update'),
]
