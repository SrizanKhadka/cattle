from rest_framework.views import APIView
from rest_framework import viewsets
from authentication.api.serailizers import UserSerializer
from authentication.models import UserModel
from rest_framework import permissions

class RegisterAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]
    
        