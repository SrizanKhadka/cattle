from rest_framework import viewsets
from cattlesection.api.serializers import CattleSerializer
from cattlesection.models import UserModel
from rest_framework import permissions

class CattleDetailsView(viewsets.ModelViewSet):
    serializer_class = CattleSerializer
    queryset = UserModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]