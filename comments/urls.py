from django.urls import path

from .views import CreateCommentView, CreateChildComment

app_name = 'comments'
urlpatterns = [
    path('comments/create/<str:slug>/', CreateCommentView.as_view(), name='comment_create'),
    path('comments/child/create/', CreateChildComment.as_view(), name='comment_child_create'),
]
