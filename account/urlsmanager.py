from django.urls import path

from account.apps import AccountConfig
from . import views

app_name = AccountConfig.name
urlpatterns = [
    path(r'login/', views.login, name='login'),
    path(r'logout/', views.logout, name='logout'),
]
