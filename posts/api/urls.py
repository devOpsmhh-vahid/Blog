from django.urls import path
from posts.api.views import (PostListCreateView, PostDetailView, RepostListCreateView)


app_name = 'post-api'
urlpatterns = [
    path('list/', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('repost/list/', RepostListCreateView.as_view(), name="repost-list"),
    
]
