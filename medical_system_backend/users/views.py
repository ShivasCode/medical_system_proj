from django.shortcuts import render

from rest_framework import generics,permissions
from rest_framework.response import Response

from django.conf import settings



from .serializers import PatientSerializer, DoctorRegistrationSerializer, DoctorLoginSerializer
from .models import CustomUser, Doctor
import random
import string
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login

from django.shortcuts import get_object_or_404


from management.models import Schedule, Pre_assessment, Appointment
from rest_framework.exceptions import NotFound

from rest_framework import status


class PatientRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.AllowAny,)


    def generate_verification_code(self):
        characters = string.ascii_letters + string.digits
        verification_code = ''.join(random.choices(characters, k=10))
        return verification_code

    def send_verification_email(self, recipient_email, date,verification_code):
        subject = 'Appointment Schedule'
        message = f'Thank you for choosing Chinese General Hospital, your appointment date is {date}. We will give you a notice the day before your appointment so you will not forget it. Lastly, make sure to be there early because we are strict about the time and if you miss it we will give your slot to other patients.'
        
        sender_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender_email, [recipient_email])




    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            schedule_id = request.data.get('schedule_id')
            schedule = Schedule.objects.get(id=schedule_id)
        except (Schedule.DoesNotExist, ValueError):
            raise NotFound("Invalid schedule_id")
        pre_assessment_data = {
            'primary_symptoms': request.data.get('primary_symptoms'),
            'current_medical_or_past_medical': request.data.get('current_medical_or_past_medical'),
            'drink_alcohol': request.data.get('drink_alcohol'),
            'current_medications': request.data.get('current_medications'),
            'smoker': request.data.get('smoker'),
        }

        appointment_data = {
            'start_time': request.data.get('start_time'),
            'end_time': request.data.get('end_time'),
            'weekday': request.data.get('weekday'),
            'date': request.data.get('date'),

        }

        try:
            
            verification_code = self.generate_verification_code()
            patient = serializer.save(
            verification_code=verification_code,
            is_patient=True,
            )

            user = CustomUser.objects.get(id=patient.id)

            pre_assessment = Pre_assessment.objects.create(user=user,**pre_assessment_data)
            Appointment.objects.create(user=user,**appointment_data,schedule=schedule,pre_assessment=pre_assessment)
            # print(patient.email)
            self.send_verification_email(patient.email,request.data.get('date'), verification_code)

            return Response(
                {"message": "Registration successful"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )



class PatientLoginView(generics.GenericAPIView):
    serializer_class = PatientSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        verification_code = request.data.get('verification_code')

        if not verification_code:
            return Response({'error': 'Verification code is required.'}, status=400)

        user = authenticate(request, verification_code=verification_code)

        if user is None:
            return Response({'error': 'Invalid verification code.'}, status=400)

        login(request, user)

        return Response({'success': 'Logged in successfully.'})

class DoctorRegistrationView(generics.CreateAPIView):
    serializer_class = DoctorRegistrationSerializer
    permission_classes = (permissions.AllowAny,)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            doctor = serializer.save(
                is_doctor=True
            )
            user = CustomUser.objects.get(id=doctor.id)
            Doctor.objects.create(user=user)
            return Response(
                {"message": "Registration successful"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )    
        
# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView

# class DoctorLoginView(APIView):
#     serializer_class = DoctorLoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, _ = Token.objects.get_or_create(user=user)  

#         return Response({"token": token.key}, status=status.HTTP_200_OK)
