from rest_framework import serializers
from .models import Item
from fields.fields import Base64ImageField

class ItemSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Item
        fields = "__all__"

