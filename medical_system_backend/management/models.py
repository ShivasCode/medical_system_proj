from django.db import models
from django.conf import settings
# Create your models here.


class Schedule(models.Model):
    doctor = models.ForeignKey(to='users.Doctor', on_delete=models.CASCADE,related_name='schedule_doctor', blank=True,null=True)
    weekday = models.IntegerField(blank=True,null=True,choices=((1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')))
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    taken = models.BooleanField(default=False)
    

class Pre_assessment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,null=True, on_delete=models.CASCADE)
    primary_symptoms = models.CharField(max_length=255, blank=True,null=True)
    current_medical_or_past_medical = models.CharField(max_length=255, blank=True,null=True)
    drink_alcohol = models.CharField(max_length=255, blank=True,null=True)
    current_medications = models.CharField(max_length=255, blank=True,null=True)
    smoker = models.BooleanField(blank=True,null=True, default=False)

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,null=True, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True,null=True)
    end_time = models.TimeField(blank=True,null=True)
    weekday = models.IntegerField(blank=True,null=True,choices=((1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')))
    date = models.DateField(blank=True,null=True)
    approved = models.BooleanField(default=False)
    schedule = models.ForeignKey(Schedule, related_name='appointment_schedule', on_delete=models.SET_NULL, blank=True, null=True)
    pre_assessment = models.ForeignKey(Pre_assessment, related_name='appointment_pre_assessment', on_delete=models.SET_NULL, blank=True, null=True)
