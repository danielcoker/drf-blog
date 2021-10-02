from rest_framework import serializers

from authentication.models import User
from authentication.serializers import UserSerializer

from posts.models import Comment, Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False, read_only=True)
    author = UserSerializer(required=False, read_only=True)
    image = serializers.URLField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'tags', 'author', 'image',)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'body', 'author',)
