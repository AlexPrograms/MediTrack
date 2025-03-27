from django.db import models
from apps.home.models import User  # Import the custom User model
from django.conf import settings


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={"role": "patient"})
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, null=True, choices=(("male", "Male"), ("female", "Female"),
                                                      ("other", "Other")))

    # Medical Details
    medical_history = models.TextField(blank=True, null=True)  # Past illnesses, treatments, surgeries
    current_condition = models.TextField(blank=True, null=True)  # Ongoing conditions
    allergies = models.TextField(blank=True, null=True)  # List of allergies
    medications = models.TextField(blank=True, null=True)  # Current medications
    blood_type = models.CharField(max_length=3, choices=[
        ("A+", "A+"), ("A-", "A-"), ("B+", "B-"),
        ("O+", "O+"), ("O-", "O-"), ("AB+", "AB-")
    ], blank=True, null=True)

    # Vitals and Health Data
    weight = models.FloatField(blank=True, null=True)  # kg
    height = models.FloatField(blank=True, null=True)  # cm
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)  # Example: "120/80 mmHg"
    heart_rate = models.PositiveIntegerField(blank=True, null=True)  # Beats per minute
    cholesterol_level = models.FloatField(blank=True, null=True)  # mg/dL
    glucose_level = models.FloatField(blank=True, null=True)  # mg/dL

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
