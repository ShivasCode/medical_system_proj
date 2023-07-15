from rest_framework import serializers

from .models import CustomUser, Doctor
from management.models import Schedule


class CustomTimeField(serializers.TimeField):
    def to_representation(self, value):
        formatted_time = value.strftime('%I:%M %p')
        return formatted_time


class ScheduleSerializer(serializers.ModelSerializer):
    # doctor = DoctorSerializer()
    start_time = CustomTimeField()
    end_time = CustomTimeField()
    class Meta:
        model = Schedule
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password',)

class DoctorInfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name','email','last_name','mobile_number','profile_pic','doctor_type'
            )




class DoctorSerializer(serializers.ModelSerializer):
    user = DoctorInfosSerializer()
    schedules = ScheduleSerializer(source='schedule_doctor', many=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('id','email','first_name','last_name','mobile_number','doctor_type','password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance


from django.contrib.auth import authenticate

class DoctorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must provide email and password.")

        data['user'] = user
        return data
    
