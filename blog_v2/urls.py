from django.contrib.auth.decorators import login_required
from django.urls import path

from blog_v2.apps import BlogV2Config
from blog_v2.views import ServiceView

app_name = BlogV2Config.name
urlpatterns = [
    path(r'', login_required(ServiceView.as_view()), name='index'),
]
