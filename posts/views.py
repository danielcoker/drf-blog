from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from base.mixins import SuccessMessageMixin

from .models import Comment, Post
from .serializers import PostSerializer, CommentSerializer


class PostListCreateAPIView(SuccessMessageMixin, ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.active()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(SuccessMessageMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.active()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentListCreateAPIView(SuccessMessageMixin, ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Comment.objects.filter(post__id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)
