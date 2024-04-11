from rest_framework import serializers
from cattlesection.models import *

class CattleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CattleModel
        fields = "__all__"


