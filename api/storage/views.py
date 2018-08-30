from rest_framework import viewsets, permissions

from api.storage.serializers import FileModelSerializer
from storage.models import FileModel


class FileModelReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows files to be viewed.
    """
    queryset = FileModel.objects.all()
    serializer_class = FileModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
