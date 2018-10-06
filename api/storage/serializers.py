from rest_framework import serializers

from storage.models import FileModel


class FileSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(write_only=True)
    file_name = serializers.SerializerMethodField()
    download_link = serializers.SerializerMethodField('get_file_uri')

    class Meta:
        model = FileModel
        fields = ('url', 'title', 'notes', 'upload_date', 'count', 'file', 'file_name', 'download_link')
        read_only_fields = ('count',)

    def get_file_uri(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.url)

    def get_file_name(self, obj):
        return obj.file_name
