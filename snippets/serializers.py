<<<<<<< HEAD
from rest_framework import serializers
from snippets.models import Snippets
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippets
        fields = ['url', 'id', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets-detail', read_only=True)

    class Meta:
        model = User
=======
from rest_framework import serializers
from snippets.models import Snippets
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippets
        fields = ['url', 'id', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets-detail', read_only=True)

    class Meta:
        model = User
>>>>>>> ef79b1ff6dcedc869fb8a3aa05a89cc0dc427a68
        fields = ['url', 'id', 'username', 'snippets']