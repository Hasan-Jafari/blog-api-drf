from rest_framework import serializers

from .category import CategorySerializer
from .tag import TagSerializer
from core.models import Post



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author', 'categories', 'tags',
            'content', 'status', 'views_count', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'slug', 'author', 'status',
            'views_count', 'created_at', 'updated_at'
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('Title cannot be empty.')
        return value

    def validate_content(self, value):
        if len(value.strip()) < 20:
            raise serializers.ValidationError('Content is too short.')
        return value
