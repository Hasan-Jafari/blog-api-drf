from rest_framework_nested import routers

from api.views.post import PostViewSet
from api.views.comment import CommentViewSet



router = routers.DefaultRouter()

app_name = 'post'
router.register(r'', PostViewSet, basename='post')
router.register('', PostViewSet, basename='post')

posts_router = routers.NestedDefaultRouter(router, r'', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = router.urls + posts_router.urls
