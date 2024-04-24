from rest_framework import viewsets
from cattlesection.api.serializers import *
from authentication.api.serailizers import UserSerializer
from cattlesection.models import CattleModel
from rest_framework import permissions
from cattlesection.api import permission
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters



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


def calculate_body_weight(self,hearth_girth):
    return hearth_girth + 5

def get_animal_code(self, animal_id):
        animal = CattleModel.objects.filter(id=animal_id).first()
        if animal:
            return animal.id_name
        return None


class WeightDetailsView(viewsets.ModelViewSet):
    serializer_class = WeightSerializer
    queryset = Weight.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('animal_id',)

    def perform_create(self, serializer):
        heartGirth = self.request.data['heart_girth']
        animal_id = self.request.data['animal_id']

        animal_code = get_animal_code(self=self,animal_id=animal_id)
        weight = calculate_body_weight(self=self,hearth_girth=heartGirth)

        serializer.validated_data['animal_code'] = animal_code              
        serializer.validated_data['body_weight'] = weight
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permission.IsCattleOwner]
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        heartGirth = self.request.data['heart_girth']
        animal_id = self.request.data['animal_id']

        animal_code = get_animal_code(self=self,animal_id=animal_id)
        weight = calculate_body_weight(self=self,hearth_girth=heartGirth)

        serializer.is_valid(raise_exception=True)

        serializer.validated_data['body_weight'] = weight
        serializer.validated_data['animal_code'] = animal_code              

        self.perform_update(serializer=serializer)

        return Response(
            {"data": serializer.data, "message": "Weight Updated Successfully!"}
        )

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permission.IsCattleOwner]
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Weight Deleted Successfully!"})

class MatingDetailsView(viewsets.ModelViewSet):
    serializer_class = MatingSerializer
    queryset = Mating.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('animal_id',)

    def perform_create(self, serializer):
        animal_id = self.request.data['animal_id']
        animal_code = get_animal_code(self=self,animal_id=animal_id)

        serializer.validated_data['animal_code'] = animal_code 

        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        serializer =  super().update(request, *args, **kwargs)

        return Response(
            {"data": serializer.data, "message": "Mating Updated Successfully!"}
        )

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permission.IsCattleOwner]
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Mating Deleted Successfully!"})