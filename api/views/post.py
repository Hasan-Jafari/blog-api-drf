from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Post
from core.serializers import PostSerializer
from core.paginations import CustomPaginator
from core.filters import PostFilter



class PostViewSet(ModelViewSet):
    queryset = (
        Post.objects
        .select_related('author')
        .prefetch_related('categories', 'tag')
        .prefetch_related('categories', 'tags')
        .all()
    )
    serializer_class = PostSerializer
    pagination_class = CustomPaginator
    permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        serializer.save(author=self.request.user)