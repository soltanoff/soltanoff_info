from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from api.permissions import IsStaffOrReadOnly
from api.post.serializers import PostSerializer, TagSerializer
from blog.models import PostModel, TagModel


class PostViewListSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsStaffOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def content(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.entry + post.content)


class TagViewListSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated, IsStaffOrReadOnly,)
