from django.urls import path

from .views import BaseView, VideoDetailView

app_name = 'main'
urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('video/<str:slug>/', VideoDetailView.as_view(), name='video_detail'),
]
