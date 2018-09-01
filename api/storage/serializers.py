from rest_framework import serializers

from storage.models import FileModel


class FileModelSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.SerializerMethodField('get_file_uri')
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = FileModel
        fields = ('url', 'title', 'notes', 'upload_date', 'count', 'file', 'file_name')

    def get_file_uri(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_url())

    def get_file_name(self, obj):
        return obj.file_name
