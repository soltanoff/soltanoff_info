from collections import OrderedDict

from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.permissions import IsStaffOrReadOnly
from api.post.serializers import PostSerializer, TagSerializer
from blog.models import PostModel, TagModel


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('count_pages', self.page.paginator.num_pages),
            ('next_page', self.page.next_page_number() if self.page.has_next() else None),
            ('previous_page', self.page.previous_page_number() if self.page.has_previous() else None),
            ('results', data),
        ]))

class PostViewListSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsStaffOrReadOnly,)
    pagination_class = StandardResultsSetPagination

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
