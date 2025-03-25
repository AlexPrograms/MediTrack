
from django.db import models
from django.contrib.auth.models import User

#models
class Appointment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apointments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apointments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apointments')