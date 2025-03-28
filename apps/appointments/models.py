
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now


#models
class Appointment(models.Model):
    STATUS_SCHEDULED = "scheduled"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = [
        (STATUS_SCHEDULED, "Scheduled"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELED, "Canceled"),
    ]

    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_SCHEDULED)
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'doctor'},
        related_name="appointments_as_doctor",  # Avoids clash
        default=1,
    )

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'patient'},
        related_name="appointments_as_patient",
        default=1,
    )

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.username} - {self.patient.username} on {self.date}"

    @property
    def dynamic_status(self):
        """Automatically determines the status based on the date."""
        if self.status != self.STATUS_CANCELED and self.date < now():
            return self.STATUS_COMPLETED
        return self.status






