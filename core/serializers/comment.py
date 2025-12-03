from rest_framework import serializers

from core.models import Comment



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id', 'author', 'post', 'content',
            'approved', 'created_at', 'updated_at'
        ]

        read_only_fields = ['id', 'author', 'approved', 'created_at', 'updated_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError('Comment content cannot be empty.')
        return value
