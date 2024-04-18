from rest_framework import viewsets
from cattlesection.api.serializers import CattleSerializer
from authentication.api.serailizers import UserSerializer
from cattlesection.models import CattleModel
from rest_framework import permissions
from cattlesection.api import permission
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CattleDetailsView(viewsets.ModelViewSet):
    serializer_class = CattleSerializer
    queryset = CattleModel.objects.all()
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    permission_classes = [permissions.IsAuthenticated]

    def modify_id_name(self, serializer):
        user_serializer = UserSerializer(self.request.user)
        household_name = user_serializer.data["household_name"]
        animalId = self.request.data.get("id_name")
        print(f'ANIMAL ID = {animalId}')
        print(f'HOUSEHOLD NAME = {household_name}')
        animalCode = f"{household_name} - {animalId}"
        return animalCode

    def perform_create(self, serializer):
        serializer.validated_data["id_name"] = self.modify_id_name(serializer=serializer)
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permission.IsCattleOwner]
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["id_name"] = self.modify_id_name(serializer=serializer)
        self.perform_update(serializer=serializer)
        return Response(
            {"data": serializer.data, "message": "Cattle Updated Successfully!"}
        )

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permission.IsCattleOwner]
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Cattle Deleted Successfully!"})
