from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'specialization', 'experience_years', 'phone', 'available']
        read_only_fields = ['user']  # Only admin can assign users        fields = ['id', 'name', 'specialization', 'experience_years', 'available']