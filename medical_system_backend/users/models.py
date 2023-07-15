from django.db import models

from management.models import Schedule

from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):

    CHOICES_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    CHOICES_TYPE = (
        ('Cardiologist', 'Cardiologist'),
        ('Neurologist', 'Neurologist'),
        ('Radiologist', 'Radiologist'),
        ('Surgeon', 'Surgeon'),
        ('Pediatrician', 'Pediatrician'),
        ('Dermatologist', 'Dermatologist'),

    )

    username = None

    first_name = models.CharField(max_length=255)   
    middle_name = models.CharField(max_length=255, blank=True,null=True)   
    email = models.EmailField(_('email address'), unique=True)  
    last_name = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True,default=1)
    pwd = models.BooleanField(blank=True,null=True,default=False)
    gender = models.CharField(max_length=255, choices=CHOICES_GENDER, blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    mobile_number = models.CharField(max_length=255,blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    height = models.IntegerField(blank=True,null=True)
    is_doctor = models.BooleanField(blank=True,null=True,default=False)
    is_patient = models.BooleanField(blank=True,null=True,default=False)
    verification_code = models.CharField(max_length=10, null=True, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images/',blank=True,null=True)
    doctor_type = models.CharField(max_length=255,choices=CHOICES_TYPE,blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()





class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='doctor_user', blank=True,null=True)
    patients = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='doctor_patients',blank=True)

    def __str__(self):
        return self.user.email

