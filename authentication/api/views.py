from rest_framework.views import APIView
from rest_framework import viewsets
from authentication.api.serailizers import UserSerializer, LoginSerializer
from authentication.models import UserModel
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class RegisterAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]
    
class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer       
