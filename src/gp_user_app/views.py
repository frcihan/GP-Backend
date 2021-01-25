from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from gp_blog_app import serializers
from rest_framework import status
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer, ProfileSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(["GET", "PUT"])
def Profile_get_update(request):
    # profile = get_object_or_404(Profile, user__id=id)
    if request.method == "GET":
        serializer = ProfileSerializer(request.user.profile)

        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProfileSerializer(request.user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Profile updated succesfully!"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

