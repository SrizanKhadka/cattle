from typing import Any
from django.db import models
from authentication.models import UserModel

# Create your models here.

SPECIES = [
    ("CATTLE", "cattle"),
    ("BUFFALO", "buffalo")
]

BREEDS = [
    ("JX", "jx"),
    ("HFX", "hfx"),
    ("L", "l"),
    ("O", "o"),
    ("MX", "mx"),
    ("L", "l"),
    ("O", "o")
]

MATING_TYPE = [
    ("ARTIFICAL INSEMINATION", "AI"),
    ("NATURAL SERVICE", "NS")
]


class CattleModel(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name='user', null=True)
    id_name = models.CharField(max_length=30)
    species = models.CharField(max_length=30, choices=SPECIES)
    breed = models.CharField(max_length=30, choices=BREEDS)
    dob = models.DateField()
    sireId = models.CharField(max_length=30)
    damId = models.CharField(max_length=30)

    def __str__(self):
        return self.id_name

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._meta.get_field('breed').choices = self.get_breed_choices()

    # def get_breed_choices(self):
    #     if(self.species == 'CATTLE'):
    #         return CATTLE_BREED
    #     else:
    #         return BUFFALO_BREED


class Weight(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name='weight_user', null=True)
    animal_id = models.IntegerField()
    animal_code = models.CharField(max_length=30, null=True, blank=True)
    body_weight = models.IntegerField(null=True, blank=True)
    heart_girth = models.IntegerField()
    weight_date = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.animal_code


class Mating(models.Model):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="mating_user", null=True)
    mating_date = models.CharField(max_length=30)
    animal_id = models.IntegerField()
    animal_code = models.CharField(max_length=30, default="")
    mating_type = models.CharField(max_length=30, choices=MATING_TYPE)
    bull_number = models.CharField(max_length=30, default="",blank=True)
    semen_number = models.CharField(max_length=30, default="",blank=True)
    expected_doc = models.CharField(max_length=30, default="",blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.animal_id

class PregnancyDetection(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="pregnancy_detection_user",null=True)
    test_date = models.CharField(max_length=30)
    animal_code = models.CharField(max_length=30,default="",blank=True)
    animal_id = models.IntegerField()
    result = models.BooleanField()
    technician_name = models.CharField(max_length=30)
    expected_doc = models.CharField(max_length=30,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # When this option is set, the field will be set to the current date and time when an object is created for the first time.
    # Once set during the creation, it won't change subsequently when the object is updated.
    updated_date = models.DateTimeField(auto_now=True)
    # When this option is set, the field will be updated to the current date and time every time the object is saved
    # This means that every time you call save() on the model instance, the updated_date field will be updated.
    

    def __str__(self):
        return self.technician_name