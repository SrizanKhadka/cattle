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
        read_only_fields = ('body_weight','animal_code')

    def validate(self, data):
        heart_girth = data.get('heart_girth')
        if not (63 <= heart_girth <= 232):
         raise ValidationError("Heart girth must be between 63 and 232")
        return data


class MatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mating
        fields = "__all__"
        read_only_fields = ('expected_doc','animal_code')

    
    def validate(self, data):
        mating_type = data.get('mating_type')
        semen_number = data.get('semen_number', "")
        bull_number = data.get('bull_number', "")

        if mating_type == 'ARTIFICIAL INSEMINATION' and not semen_number:
            raise ValidationError("Semen number is required!")

        if mating_type == 'NATURAL SERVICE' and not bull_number:
            raise ValidationError("Bull number is required!")

        return data

