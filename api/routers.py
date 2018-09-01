from rest_framework import routers

from api.storage import views as storage_views
from api.users import views as users_views

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'users/groups', users_views.GroupViewSet)  # TODO: http://www.django-rest-framework.org/api-guide/routers/#api-guide
router.register(r'storage', storage_views.FileViewSet)
