from django.db import models
from apps.home.models import User  # Import the custom User model

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={"role": "doctor"})
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    experience_years = models.PositiveIntegerField()

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialization}"
