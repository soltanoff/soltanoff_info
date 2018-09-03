from rest_framework import serializers

from blog.models import PostModel, TagModel


class PostSerializer(serializers.HyperlinkedModelSerializer):
    entry = serializers.Field(write_only=True)
    content = serializers.HyperlinkedIdentityField(view_name='post-content', format='html', read_only=True)
    tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail', read_only=True)
    tags_names = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ('url', 'title', 'datetime', 'tags', 'tag_names', 'entry', 'content')
        read_only_fields = ('datetime',)

    def get_tags_names(self, obj):
        return ','.join(map(lambda x: "'%s'" % x.title, obj.tags))


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagModel
        fields = ('url', 'title', 'datetime', 'description')
        read_only_fields = ('datetime',)
