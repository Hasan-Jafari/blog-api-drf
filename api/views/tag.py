from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Tag, Post
from core.serializers import TagSerializer, PostSerializer
from core.paginations import CustomPaginator

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPaginator
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        tag = self.get_object()
        posts = (
            Post.objects
            .filter(tag=tag)
            .select_related('author')
            .prefetch_related('categories', 'tag')
        )
        page = self.paginate_queryset(posts)
        serializer = PostSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
