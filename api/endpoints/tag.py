from rest_framework.routers import DefaultRouter

from api.views import TagViewSet



router = DefaultRouter()

app_name = 'tag'
router.register(r'', TagViewSet, basename='tag')

urlpatterns = router.urls
