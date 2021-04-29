from  django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, filters
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, GroupSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username', 'email', 'groups']

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filterset_fields = ['name']
