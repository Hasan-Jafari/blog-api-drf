from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet



router = DefaultRouter()

app_name = 'category'
router.register(r'', CategoryViewSet, basename='category')

urlpatterns = router.urls
