from django.contrib import admin

# Register your models here.
from .models import Schedule, Pre_assessment, Appointment

admin.site.register(Schedule)
admin.site.register(Pre_assessment)
admin.site.register(Appointment)