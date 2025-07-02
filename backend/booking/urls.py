from django.urls import path
from .views import (
    StudentRegistrationView, FacultyRegistrationView,
    SendOTPView, VerifyOTPView, LoginView
)

urlpatterns = [
    path('register/student/', StudentRegistrationView.as_view(), name='register-student'),
    path('register/faculty/', FacultyRegistrationView.as_view(), name='register-faculty'),
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('login/', LoginView.as_view(), name='login'),
] 