from django.shortcuts import get_object_or_404
from .models import Blog, Like, Comment, Category, BlogView

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogListSerializer, BlogCreateUpdateSerializer, BlogDetailSerializer, CommentCreateSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwner
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

class BlogUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    lookup_field = "slug"

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
class BlogDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = "slug"
    

class CreateCommentAPI(APIView):
    """
    blog:
        Create a comment instnace. Returns created comment data
        parameters: [slug, body]
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer
    # permission_classes = [IsAuthenticated]

    def blog(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, blog=blog)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)


class CreateLikeAPI(APIView):

    # serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def blog(self, request, slug):
        obj = get_object_or_404(Blog, slug=slug)
        like_qs = Like.objects.filter(user=request.user, blog=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, blog=obj)

        data = {
            "messages": "like"
        }
        return Response(data)


