from rest_framework import serializers
from .models import Appointment
from apps.doctors.serializers import DoctorSerializer
from apps.patients.serializers import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    patient_details = PatientSerializer(source='patient', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date', 'status', 'description',
                 'doctor_details', 'patient_details']
        read_only_fields = ['status']  # Status can only be changed through specific actions
