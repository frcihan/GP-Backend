from django.shortcuts import get_object_or_404
from .models import Blog, Like, Comment, Category, BlogView

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogListSerializer, BlogCreateUpdateSerializer
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
    
@api_view(["GET", "PUT", "DELETE"])
def student_get_update_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "GET":
        serializer = BlogListSerializer(blog)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = BlogListSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message" : "Blog updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
