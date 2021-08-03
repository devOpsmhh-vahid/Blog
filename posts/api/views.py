from django.db.models.query_utils import Q
from django.shortcuts import render
from posts.api.serializers import PostSerializer
from posts.models import (PostModel)
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
# Create your views here.


class PostListCreateView(ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    

    filterset_fields = ['title']
    search_fields    = ['title']
    ordering_fields  = ['created_at']


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class RepostListCreateView(ListCreateAPIView):
    queryset = PostModel.objects.filter(post_type=2)
    serializer_class = PostSerializer
    