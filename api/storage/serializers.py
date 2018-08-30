from rest_framework import serializers

from storage.models import FileModel


class FileModelSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = FileModel
        fields = ('title', 'notes', 'upload_date', 'count', 'file')

    def get_file(self, obj):
        return obj.get_url()

    def get_file_name(self, obj):
        return obj.file_name
