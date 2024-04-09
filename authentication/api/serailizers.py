from typing import Any, Dict
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from authentication.models import UserModel
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        # fields = "__all__"
        extra_kwargs = {
            'password':{'write_only': True},
            'password_confirm':{'write_only': True}
        }
        exclude = ("user_permissions","groups")

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
    
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
class LoginSerializer(TokenObtainPairSerializer):

    def validate(self,attrs):
        attrs = super().validate(attrs)
        userData = UserSerializer(self.user)
        token = self.get_token(self.user)
        access_token = str(token.access_token)
        refresh_token = str(token)
        print(F"TOKEN = {self.get_token(self.user)}")
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user_data': userData.data,
        }
