from rest_framework import routers

from posts.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='post-comments')
