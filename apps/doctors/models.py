from django.db import models
from apps.core.models import User  # Import the custom User model
from django.conf import settings

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="doctor",
                                limit_choices_to={"role": "doctor"})
    specialization = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialization}"

