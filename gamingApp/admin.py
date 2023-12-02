from django.contrib import admin
from .models import models
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(GameModel)
admin.site.register(Snippet)

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

# admin.site.register(CustomUser, UserModel)