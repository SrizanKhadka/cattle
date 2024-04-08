from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserModel(AbstractUser):
    role = models.CharField(max_length=255)
    password_confirm = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=255,unique=True)
    household_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    household_no = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True)
    
    USERNAME_FIELD = 'mobile_number' 
    REQUIRED_FIELDS = ['username']
    
    #If the REQUIRED_FIELDS list is empty in your Django custom user model, 
    #it means there are no additional required fields apart from the default ones (username and password) when creating a new user.

    def __str__(self):
        return self.mobile_number
