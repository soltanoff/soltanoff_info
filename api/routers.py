from rest_framework import routers

from api.post import views as post_views
from api.storage import views as storage_views
from api.users import views as users_views

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'users/groups', users_views.GroupViewSet)
router.register(r'post', post_views.PostViewListSet)
router.register(r'post/tags', post_views.TagViewListSet)
router.register(r'storage', storage_views.FileViewSet)
