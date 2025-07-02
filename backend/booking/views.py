from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Faculty, OTP
from .serializers import (
    StudentSerializer, StudentRegistrationSerializer,
    FacultySerializer, FacultyRegistrationSerializer,
    OTPSerializer, LoginSerializer
)
from django.utils.crypto import get_random_string
from django.db import IntegrityError

# Create your views here.

# Faculty adds student (default password Student@123)
class StudentRegistrationView(APIView):
    def post(self, request):
        serializer = StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                student = Student.objects.create(
                    name=serializer.validated_data['name'],
                    email=serializer.validated_data['email'],
                    mobile=serializer.validated_data['mobile'],
                    device_token=serializer.validated_data.get('device_token'),
                    password='Student@123',
                )
                return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'error': 'Student with this email or mobile already exists.'}, status=400)
        return Response(serializer.errors, status=400)

# Faculty registration
class FacultyRegistrationView(APIView):
    def post(self, request):
        serializer = FacultyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                faculty = Faculty.objects.create(
                    name=serializer.validated_data['name'],
                    email=serializer.validated_data['email'],
                    mobile=serializer.validated_data['mobile'],
                    device_token=serializer.validated_data.get('device_token'),
                    password=serializer.validated_data['password'],
                )
                return Response(FacultySerializer(faculty).data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'error': 'Faculty with this email or mobile already exists.'}, status=400)
        return Response(serializer.errors, status=400)

# Send OTP for mobile login
class SendOTPView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        if not mobile:
            return Response({'error': 'Mobile number required.'}, status=400)
        otp_code = get_random_string(length=6, allowed_chars='0123456789')
        OTP.objects.create(mobile=mobile, otp_code=otp_code)
        # In production, send OTP via SMS gateway here
        return Response({'message': f'OTP sent to {mobile}', 'otp': otp_code}, status=200)

# Verify OTP
class VerifyOTPView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        otp_code = request.data.get('otp_code')
        try:
            otp = OTP.objects.filter(mobile=mobile, otp_code=otp_code, is_verified=False).latest('created_at')
        except OTP.DoesNotExist:
            return Response({'error': 'Invalid OTP.'}, status=400)
        otp.is_verified = True
        otp.save()
        # Optionally, log the user in or return a token
        return Response({'message': 'OTP verified.'}, status=200)

# Login (email/password or mobile/OTP)
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            mobile = serializer.validated_data.get('mobile')
            otp_code = serializer.validated_data.get('otp_code')
            # Email/password login
            if email and password:
                user = Student.objects.filter(email=email, password=password).first() or \
                       Faculty.objects.filter(email=email, password=password).first()
                if user:
                    return Response({'message': 'Login successful', 'user_id': user.id, 'role': 'faculty' if isinstance(user, Faculty) else 'student'}, status=200)
                return Response({'error': 'Invalid credentials.'}, status=400)
            # Mobile/OTP login
            if mobile and otp_code:
                otp = OTP.objects.filter(mobile=mobile, otp_code=otp_code, is_verified=True).order_by('-created_at').first()
                if otp:
                    user = Student.objects.filter(mobile=mobile).first() or Faculty.objects.filter(mobile=mobile).first()
                    if user:
                        return Response({'message': 'Login successful', 'user_id': user.id, 'role': 'faculty' if isinstance(user, Faculty) else 'student'}, status=200)
                    return Response({'error': 'User not found.'}, status=404)
                return Response({'error': 'Invalid or unverified OTP.'}, status=400)
            return Response({'error': 'Provide email/password or mobile/otp_code.'}, status=400)
        return Response(serializer.errors, status=400)
