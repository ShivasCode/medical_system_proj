from django.contrib import admin

# Register your models here.
from .models import CustomUser, Doctor

admin.site.register(CustomUser)
admin.site.register(Doctor)