from django.urls import path, include



app_name = 'api'
urlpatterns = [
    path('category/', include('api.endpoints.category', namespace='category')),
    path('post/', include('api.endpoints.post', namespace='post')),
    path('tag/', include('api.endpoints.tag', namespace='tag')),
]
