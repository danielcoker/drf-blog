from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from base.mixins import SuccessMessageMixin

from .models import Post
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


class CommentCreateAPIView(SuccessMessageMixin, CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)
