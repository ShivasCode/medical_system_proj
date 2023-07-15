from django.urls import path
from .views import AvailableDoctorsListView,DoctorPatientListView,DisapprovePatientAppointment

urlpatterns = [
    
    path('available-doctors/', AvailableDoctorsListView.as_view(), name='available-doctors-list'),
    path('doctors/patients/', DoctorPatientListView.as_view(), name='doctor-patient-list'),
    path('appointment-disapproval/<int:id>/', DisapprovePatientAppointment.as_view(), name='appointment-disapproval'),

]