from django.urls import path
from users.api.views import (UserListCreateView, UserDetailView)
app_name = 'user-api'
urlpatterns = [
    path('list/', UserListCreateView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
]
