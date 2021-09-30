from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from base.mixins import SuccessMessageMixin

from .models import Post
from .serializers import PostSerializer


class PostListCreateAPIView(SuccessMessageMixin, ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.active()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
