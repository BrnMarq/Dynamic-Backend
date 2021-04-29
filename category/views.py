from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets, permissions

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
