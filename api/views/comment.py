from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from core.models import Comment
from core.serializers import CommentSerializer
from core.paginations import CustomPaginator



class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CustomPaginator
    permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return (
            Comment.objects
            .filter(post_id=post_id)
            .select_related('author', 'post')
        )

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        serializer.save(author=self.request.user, post_id=post_id)
