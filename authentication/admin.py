from django.contrib import admin
from authentication.models import UserModel
from django.contrib.auth.admin import UserAdmin


# Register your models here.


admin.site.register(UserModel)