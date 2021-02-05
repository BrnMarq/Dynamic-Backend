from .models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets, permissions

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
