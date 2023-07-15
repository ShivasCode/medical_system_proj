from django.urls import path
from .views import PatientRegistrationView, PatientLoginView, DoctorRegistrationView

urlpatterns = [
    path('register/', PatientRegistrationView.as_view(), name='patient-register'),
    path('login/', PatientLoginView.as_view(), name='patient-login'),
    path('doctor-register/', DoctorRegistrationView.as_view(), name='doctor-register'),

]