from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.home.models import User  # Import the actual User model
from apps.doctors.models import Doctor
from apps.patients.models import Patient

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # Runs only when a new user is created
        if instance.role == "doctor" and not hasattr(instance, 'doctor'):
            Doctor.objects.create(user=instance)
        elif instance.role == "patient" and not hasattr(instance, 'patient'):
            Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.role == "doctor" and hasattr(instance, 'doctor'):
        instance.doctor.save()
    elif instance.role == "patient" and hasattr(instance, 'patient'):
        instance.patient.save()
