from rest_framework import generics
from .models import Schedule, Appointment
from .serializers import DoctorPatientSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.serializers import ScheduleSerializer
from rest_framework.views import APIView
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.response import Response
from users.serializers import DoctorSerializer
from users.models import Doctor
from django.core.mail import send_mail

class AvailableDoctorsListView(APIView):
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        weekday = self.request.query_params.get('weekday')
        doctors = Doctor.objects.all()
        result = []

        for doctor in doctors:
            schedules = doctor.schedule_doctor.filter(weekday=weekday)
            if schedules.exists():
                doctor_data = DoctorSerializer(doctor).data
                doctor_data['schedules'] = ScheduleSerializer(schedules, many=True).data
                result.append(doctor_data)

        return Response(result)

    
class DoctorPatientListView(generics.ListAPIView):
    serializer_class = DoctorPatientSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        
        doctor_id = self.request.user.id
        return Appointment.objects.filter(schedule__doctor_id=doctor_id)

from .serializers import AppointmentSerializer
from django.shortcuts import get_object_or_404

class AppointmentRetrieveView(APIView):
    def get(self, request, id):
        appointment = get_object_or_404(Appointment, id=id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

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

class ApprovePatientAppointment(APIView):
    def send_approval_email(self, recipient_email):
        subject = 'Appointment Approval'
        message = f'Your appointment has been approved. We look forward to seeing you at the scheduled time.'
        
        sender_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender_email, [recipient_email])

    def post(self, request, id):
        appointment_id = id
        try:
            appointment = Appointment.objects.get(id=id)
            appointment.approved = True
            appointment.save()
            self.send_approval_email(appointment.user.email)
            return Response({"message": "Appointment approved"}, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)