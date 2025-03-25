from django.db import models
from apps.home.models import User  # Import the custom User model

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={"role": "patient"})
    date_of_birth = models.DateField()
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
