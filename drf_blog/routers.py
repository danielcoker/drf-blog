from rest_framework import routers

from authentication.views import AuthViewSet
from posts.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter(trailing_slash=False)

# Authentication Routes
router.register(r'users/auth', AuthViewSet, basename='auth')

# Post Routes
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='post-comments')
