from django.urls import path
from .views import AvailableDoctorsListView,DoctorPatientListView,DisapprovePatientAppointment, ApprovePatientAppointment, AppointmentRetrieveView

urlpatterns = [
    
    path('available-doctors/', AvailableDoctorsListView.as_view(), name='available-doctors-list'),
    path('doctors/patients/', DoctorPatientListView.as_view(), name='doctor-patient-list'),
    path('appointment-disapproval/<int:id>/', DisapprovePatientAppointment.as_view(), name='appointment-disapproval'),
    path('appointment-approval/<int:id>/', ApprovePatientAppointment.as_view(), name='appointment-approval'),
    path('appointments/<int:id>/', AppointmentRetrieveView.as_view(), name='appointment-retrieve'),

]