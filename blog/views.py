from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .filter import PostFilter

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    filterset_fields = ['author', 'title', 'categories']
