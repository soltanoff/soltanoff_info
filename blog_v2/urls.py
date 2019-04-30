from django.contrib.auth.decorators import login_required
from django.urls import path

from blog_v2.apps import BlogV2Config
from blog_v2.views import BlogV2View

app_name = BlogV2Config.name
urlpatterns = [
    path(r'', login_required(BlogV2View.as_view()), name='index'),
]
