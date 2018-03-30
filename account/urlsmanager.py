from django.urls import path

from account.apps import AccountConfig
from account.views import CustomLoginView
from . import views

app_name = AccountConfig.name
urlpatterns = [
    path(r'login/', CustomLoginView.as_view(), name='login'),
    path(r'logout/', views.logout, name='logout'),
]
