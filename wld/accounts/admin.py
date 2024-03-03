from django.contrib import admin

# Register your models here.
from .models import User,UserData

admin.site.register(User)
admin.site.register(UserData)