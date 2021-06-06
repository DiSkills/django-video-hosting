from django.urls import path

from .views import (
    CategoryListAPIView,
    VideoListAPIView,
    CategoryDetailAPIView,
    VideoDetailAPIView,
    BaseAPIView,
)

app_name = 'api'
urlpatterns = [
    path('', BaseAPIView.as_view(), name='base_api'),
    path('category/<int:id>/', CategoryDetailAPIView.as_view(), name='category_api'),
    path('categories/', CategoryListAPIView.as_view(), name='categories_api'),
    path('video/<int:id>/', VideoDetailAPIView.as_view(), name='video_api'),
    path('videos/', VideoListAPIView.as_view(), name='videos_api'),
]
