from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("doctor", "Doctor"),
        ("patient", "Patient"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="patient")

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_doctor(self):
        return self.role == "doctor"

    @property
    def is_patient(self):
        return self.role == "patient"
