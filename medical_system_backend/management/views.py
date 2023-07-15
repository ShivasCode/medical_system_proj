from rest_framework import generics
from .models import Schedule, Appointment
from .serializers import DoctorPatientSerializer
from rest_framework.permissions import IsAuthenticated
from users.serializers import ScheduleSerializer
from rest_framework.views import APIView
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.response import Response
from users.serializers import DoctorSerializer
from users.models import Doctor
from django.core.mail import send_mail

class AvailableDoctorsListView(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        weekday = self.request.query_params.get('weekday')

        queryset = Doctor.objects.filter(schedule_doctor__weekday=weekday).distinct()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    
class DoctorPatientListView(generics.ListAPIView):
    serializer_class = DoctorPatientSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        
        doctor_id = self.request.user.id
        return Appointment.objects.filter(schedule__doctor_id=doctor_id)
    

# @api_view(['POST'])
# def disapprove_patient_appointment(request):
class DisapprovePatientAppointment(APIView):


    def send_disapproval_email(self, recipient_email):
        subject = 'Appointment Disapproval'
        message = f'We apologize for your cancelling your appointment. The reasons might be because your late, conflict of schedule, or an emergency has happened. You can make an appointment again.'
        
        sender_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender_email, [recipient_email])

    def post(self,request,id):
        appointment_id = id
        appointment = Appointment.objects.get(id=id)
        
        appointment.delete()
        self.send_disapproval_email(appointment.user.email)         
        return Response({
            "message": "appointment disapproved",
        },  status=status.HTTP_200_OK)