from rest_framework import serializers
from .models import Student, Faculty, OTP

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'mobile', 'device_token', 'booking_limit', 'is_active', 'created_at']
        read_only_fields = ['id', 'is_active', 'created_at', 'booking_limit']

class StudentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'mobile', 'device_token']

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'email', 'mobile', 'device_token', 'is_active', 'created_at']
        read_only_fields = ['id', 'is_active', 'created_at']

class FacultyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name', 'email', 'mobile', 'password', 'device_token']
        extra_kwargs = {'password': {'write_only': True}}

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['mobile', 'otp_code', 'is_verified', 'created_at']
        read_only_fields = ['is_verified', 'created_at']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    mobile = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    otp_code = serializers.CharField(required=False) 