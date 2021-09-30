from rest_framework import serializers

from authentication.models import User
from authentication.serializers import UserSerializer

from posts.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    author = UserSerializer(required=False)
    image = serializers.URLField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'tags', 'author', 'image',)
        read_only_fields = ('id', 'author', 'tags')
