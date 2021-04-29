import django_filters
from .models import Post
from members.models import Member

class PostFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author' , lookup_expr='id__exact')

    class Meta:
        model = Post
        fields = ['title', 'author', 'categories']