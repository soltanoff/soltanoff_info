from rest_framework import serializers

from blog.models import PostModel, TagModel


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostModel
        fields = ('url', 'title', 'datetime', 'tags', 'entry', 'content')
        read_only_fields = ('datetime',)

    def get_tags_names(self, obj):
        return ','.join(map(lambda x: "'%s'" % x.title, obj.tags))


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagModel
        fields = ('url', 'title', 'datetime', 'description')
        read_only_fields = ('datetime',)
