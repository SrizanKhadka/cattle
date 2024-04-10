from django.db import models

# Create your models here.

SPECIES = [
    ("CATTLE","cattle"),
    ("BUFFALO","buffalo")
]

CATTLE_BREED = [
    ("JX","jx"),
    ("HFX","hfx"),
    ("L","l"),
    ("O","o")
]

BUFFALO_BREED = [
    ("MX","mx"),
    ("L","l"),
    ("O","o")
]


class CattleModel(models.Model):
    id_name = models.CharField(max_length=30)
    species = models.CharField(max_length=30,choices=SPECIES)
    breed = models.CharField(max_length=30,choices=CATTLE_BREED)