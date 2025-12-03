from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from core.models import Post
from core.serializers import PostSerializer
from core.paginations import CustomPaginator



class PostViewSet(ModelViewSet):
    queryset = (
        Post.objects
        .select_related('author')
        .prefetch_related('categories', 'tag')
        .all()
    )
    serializer_class = PostSerializer
    pagination_class = CustomPaginator
    permission_classes = [permissions.AllowAny]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
