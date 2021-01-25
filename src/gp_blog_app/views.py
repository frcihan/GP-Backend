from django.shortcuts import get_object_or_404
from .models import Blog, Like, Comment, Category, BlogView

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogListSerializer, BlogCreateUpdateSerializer, BlogDetailSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .pagination import BlogPageNumberPagination


# Create your views here.

class BlogList(generics.ListAPIView):

    permission_classes = [AllowAny]
    pagination_class = BlogPageNumberPagination
    serializer_class = BlogListSerializer
    queryset = Blog.objects.filter(status="d")   ############################### d or p 


class BlogCreateApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class BlogDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = "slug"

    def get_object(self):
        obj = super().get_object()
        BlogView.objects.get_or_create(user=self.request.user, blog=obj)
        return obj
