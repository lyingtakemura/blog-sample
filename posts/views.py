from rest_framework import mixins, viewsets

from posts.filters import PostFilter
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
