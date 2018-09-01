from rest_framework import viewsets, permissions
from rest_framework.parsers import FileUploadParser

from api.permissions import IsStaffOrReadOnly
from api.storage.serializers import FileSerializer
from storage.models import FileModel


class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows files to be viewed or edited.
    """
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
    permission_classes = (permissions.IsAuthenticated, IsStaffOrReadOnly,)
