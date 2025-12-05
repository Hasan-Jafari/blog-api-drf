from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions

from core.models import Category, Post
from core.serializers import CategorySerializer, PostSerializer
from core.paginations import CustomPaginator



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPaginator
    permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        category = self.get_object()
        posts = (
            Post.objects
            .filter(categories=category)
            .select_related('author')
            .prefetch_related('categories', 'tag')
            .prefetch_related('categories', 'tags')
        )
        page = self.paginate_queryset(posts)
        serializer = PostSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
