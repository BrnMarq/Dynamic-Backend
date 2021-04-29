from rest_framework import serializers
from .models import Post
from fields.fields import Base64ImageField

class PostSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image', 'author', 'categories']
