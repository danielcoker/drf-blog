from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from base.mixins import SuccessMessageMixin
from posts.permissions import IsOwnerOrReadOnly

from .models import Comment, Post
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(SuccessMessageMixin, ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.active()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(SuccessMessageMixin, ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Comment.objects.filter(post__id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)
