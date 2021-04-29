from rest_framework import serializers
from .models import Member
from fields.fields import Base64ImageField


class MemberSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Member
        fields = ['id', 'name', 'description', 'image']
