from django.urls import path

from .views import (
    BaseView,
    VideoDetailView,
    VideoStreamingResponse,
    CategoryDetailView,
    AddVideoView,
    EditVideoView,
    LikeOrDislikeView,
    VideoForSearchView,
)

app_name = 'main'
urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('video/edit/<str:slug>/', EditVideoView.as_view(), name='edit_video'),
    path('video/add/', AddVideoView.as_view(), name='add_video'),
    path('video/<str:slug>/', VideoDetailView.as_view(), name='video_detail'),
    path('video/streaming/<str:slug>/', VideoStreamingResponse.as_view(), name='video_streaming'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('likes-or-dislikes/<str:slug>', LikeOrDislikeView.as_view(), name='likes_or_dislikes'),
    path('videos/search/', VideoForSearchView.as_view(), name='search_videos'),
]
