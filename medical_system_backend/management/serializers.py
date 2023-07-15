from rest_framework import serializers
from .models import Schedule,Appointment, Pre_assessment

from users.models import Doctor, CustomUser
# from users.serializers import PatientSerializer
# from users.serializers import DoctorSerializer



class CustomTimeField(serializers.TimeField):
    def to_representation(self, value):
        formatted_time = value.strftime('%I:%M %p')
        return formatted_time


class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password',)

class PreAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pre_assessment
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    start_time = CustomTimeField()
    end_time = CustomTimeField()
    pre_assessment = PreAssessmentSerializer()
    user = PatientAppointmentSerializer()
    class Meta:
        model = Appointment
        fields = ['id', 'start_time', 'end_time', 'weekday', 'date', 'approved', 'schedule', 'pre_assessment','user']

class DoctorPatientSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer(many=True, read_only=True, source='user.appointment_set')

    class Meta:
        model = Doctor
        fields = ['id', 'appointment']