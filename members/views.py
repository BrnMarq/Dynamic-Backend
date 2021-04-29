from .models import Member
from .serializers import MemberSerializer
from rest_framework import viewsets, permissions

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filterset_fields = ['name', 'description']
    