"""django_srv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.schemas import get_schema_view

from api.routers import router as api_router

urlpatterns = [
    url(r'', include('blog.urls')),
    url(r'^v2', include('blog_v2.urls')),
    url(r'^accounts/', include('account.urls')),
    url(r'^storage/', include('storage.urls')),
    url(r'^manage/', admin.site.urls),
    url(r'^ckeditor/', (include('ckeditor_uploader.urls'))),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^schema/', get_schema_view(title='Test API')),
    url(r'^api/', include(api_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
