from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128, default='Student@123')
    device_token = models.CharField(max_length=255, blank=True, null=True)
    booking_limit = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    device_token = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class OTP(models.Model):
    mobile = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"OTP for {self.mobile}: {self.otp_code}"

class Facility(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Court(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='courts')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.facility.name} - {self.name}"

class Slot(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='slots')
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    status = models.CharField(max_length=10, choices=[('free', 'Free'), ('booked', 'Booked')], default='free')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.court} | {self.date} {self.time_start}-{self.time_end}"

class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='bookings')
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)
    cancelled = models.BooleanField(default=False)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_bookings')

    def __str__(self):
        return f"Booking: {self.student} -> {self.slot}"
