from rest_framework import serializers
from cattlesection.models import *
from rest_framework.exceptions import ValidationError


class CattleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CattleModel
        fields = "__all__"

class WeightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weight
        fields = "__all__"
def validate(self, data):
    heart_girth = data.get('heart_girth')
    if not (63 <= heart_girth <= 232):
        raise ValidationError("Heart girth must be between 63 and 232")
    return data



