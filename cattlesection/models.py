from typing import Any
from django.db import models
from authentication.models import UserModel

# Create your models here.

SPECIES = [
    ("CATTLE","cattle"),
    ("BUFFALO","buffalo")
]

BREEDS = [
    ("JX","jx"),
    ("HFX","hfx"),
    ("L","l"),
    ("O","o"),
    ("MX","mx"),
    ("L","l"),
    ("O","o")
]

# CATTLE_BREED = [
#     ("JX","jx"),
#     ("HFX","hfx"),
#     ("L","l"),
#     ("O","o")
# ]

# BUFFALO_BREED = [
#     ("MX","mx"),
#     ("L","l"),
#     ("O","o")
# ]


class CattleModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user',null=True)
    id_name = models.CharField(max_length=30)
    species = models.CharField(max_length=30,choices=SPECIES)
    breed = models.CharField(max_length=30,choices=BREEDS)
    dob = models.DateField()
    sireId = models.CharField(max_length=30)
    damId = models.CharField(max_length=30)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._meta.get_field('breed').choices = self.get_breed_choices()

    # def get_breed_choices(self):
    #     if(self.species == 'CATTLE'):
    #         return CATTLE_BREED
    #     else:
    #         return BUFFALO_BREED