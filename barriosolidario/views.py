from django.shortcuts import render

from barriosolidario.models import User, NewsPost, HelpPost
from barriosolidario.serializers import UserSerializer, NewsPostSerializer, HelpPostSerializer
from rest_framework import generics

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NewsPostListCreate(generics.ListCreateAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

class HelpPostListCreate(generics.ListCreateAPIView):
    queryset = HelpPost.objects.all()
    serializer_class = HelpPostSerializer
