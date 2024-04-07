from rest_framework import serializers
from authentication.models import UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = "__all__"

    def validate(self, data):
        role = data["role"]
        password = data['password']
        confirmPassword = data['password_confirm']

        print(f"ROLE = {role}")
        if role.lower() not in ["farmers"]:
            raise serializers.ValidationError(f'Role {role} is not a valid option. Available option farmer.')
        
        if password != confirmPassword:
            raise serializers.ValidationError(f'Password did not matched!')
        return data