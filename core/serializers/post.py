from rest_framework import serializers


from core.models import Post, Category, Tag



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author',
            'categories', 'tags','content',
            'status', 'views_count', 'created_at', 'updated_at'
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
