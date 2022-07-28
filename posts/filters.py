from django_filters import rest_framework as filters

from posts.models import Post


class PostFilter(filters.FilterSet):
    '''
    icontains - case-insensitive containment:
    SELECT ... WHERE title LIKE '%title%';

    range format:
    /?created_at_after=yyyy-mm-dd&created_at_before=yyyy-mm-dd
    '''
    title = filters.CharFilter(lookup_expr='icontains')
    body = filters.CharFilter(lookup_expr='icontains')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['title', 'body', 'created_at']
