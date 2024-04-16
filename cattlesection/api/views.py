from rest_framework import viewsets
from cattlesection.api.serializers import CattleSerializer
from authentication.api.serailizers import UserSerializer
from cattlesection.models import CattleModel
from rest_framework import permissions

class CattleDetailsView(viewsets.ModelViewSet):
    serializer_class = CattleSerializer
    queryset = CattleModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_serializer = UserSerializer(self.request.user)
        household_name = user_serializer.data['household_name']
        animalId = self.request.data.get('id_name')
        animalCode = f'{household_name} - {animalId}'
        serializer.validated_data['id_name'] = animalCode
        print(f'ANIMAL CODE = {animalCode}')
        serializer.save(user=self.request.user)