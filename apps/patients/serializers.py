from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'date_of_birth', 'age', 'blood_type', 'allergies', 
                 'blood_pressure', 'weight', 'height', 'phone']
        read_only_fields = ['user']  # Only admin can assign users
