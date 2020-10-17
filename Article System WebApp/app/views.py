from django.shortcuts import render
from django.http import *
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer,ProfileSerializer, ArticleSerializer, BuySerializer,SellSerializer
from .models import profile, article, sell,buy

# Create your views here.
User = get_user_model()

class UserRegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(self):
            serializer.save()
            return JsonResponse({'result':'sucess' , 'message':'User created successfully!'})
        return JsonResponse({'result':'error','message':'Failed!'})

class ProfileView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = profile.objects.all()
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super().get_queryset().filter(user_id=self.request.user.id)
        return super().get_queryset()

class ArticleView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArticleSerializer
    queryset = article.objects.all()
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super().get_queryset().filter(user_id=self.request.user.id)
        return super().get_queryset()

class BuyView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BuySerializer
    queryset = buy.objects.all()
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super().get_queryset().filter(user_id=self.request.user.id)
        return super().get_queryset()

class SellView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SellSerializer
    queryset = sell.objects.all()
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super().get_queryset().filter(user_id=self.request.user.id)
        return super().get_queryset()












