from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    is_staff = serializers.HyperlinkedIdentityField(view_name='user-staff', format='html')
    groups = serializers.HyperlinkedRelatedField(many=True, view_name='group-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'is_staff', 'is_superuser')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
