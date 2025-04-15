from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.db.models import Count

from apps.home.permissions import IsDoctor  # Import custom permission
from .models import Doctor
from .serializers import DoctorSerializer
from apps.appointments.models import Appointment
from apps.appointments.serializers import AppointmentSerializer
from apps.patients.models import Patient
from apps.patients.serializers import PatientSerializer
from collections import Counter
from django.db import models

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsDoctor]  # Only doctors can access
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'specialization']
    ordering_fields = ['name', 'experience_years']
    
    @action(detail=False, methods=['GET'])
    def appointments(self, request):
        """Get all appointments for the logged-in doctor"""
        doctor = request.user
        sort_by = request.query_params.get("sort", "date")
        filter_status = request.query_params.get("status", None)
        
        appointments = Appointment.objects.filter(doctor=doctor)
        
        # Apply filtering if status is provided
        if filter_status and filter_status in dict(Appointment.STATUS_CHOICES):
            appointments = appointments.filter(status=filter_status)
            
        # Apply sorting
        if sort_by == "patient":
            # This is a simplification - in a real API you might want to use annotations
            serializer = AppointmentSerializer(appointments, many=True)
            sorted_data = sorted(serializer.data, key=lambda x: x['patient_details']['name'].lower() if x.get('patient_details') else '')
            return Response(sorted_data)
        else:
            appointments = appointments.order_by('date')
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def search_patients(self, request):
        """Search for patients by name or username"""
        doctor = request.user
        query = request.query_params.get("q", "").strip().lower()
        
        # Get all patients who have appointments with this doctor
        patient_ids = Appointment.objects.filter(doctor=doctor).values_list("patient", flat=True).distinct()
        
        if query:
            patients = Patient.objects.filter(user_id__in=patient_ids).filter(
                models.Q(user__username__icontains=query) | models.Q(name__icontains=query)
            )
        else:
            patients = Patient.objects.filter(user_id__in=patient_ids)
            
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def most_frequent_patient(self, request):
        """Get the most frequent patient(s) for the logged-in doctor"""
        doctor = request.user
        appointments = Appointment.objects.filter(doctor=doctor)
        
        # Count appointments per patient
        patient_counts = Counter(a.patient_id for a in appointments)
        
        if not patient_counts:
            return Response({"message": "No patients found"}, status=status.HTTP_404_NOT_FOUND)
        
        max_count = max(patient_counts.values())
        frequent_patient_ids = [patient_id for patient_id, count in patient_counts.items() if count == max_count]
        
        patients = Patient.objects.filter(user_id__in=frequent_patient_ids)
        serializer = PatientSerializer(patients, many=True)
        
        # Include the appointment count
        result = {
            "patients": serializer.data,
            "appointment_count": max_count
        }
        
        return Response(result)
    
    @action(detail=False, methods=['GET'])
    def patients(self, request):
        """Get all patients who have appointments with the logged-in doctor"""
        doctor = request.user
        patient_ids = Appointment.objects.filter(doctor=doctor).values_list("patient", flat=True).distinct()
        patients = Patient.objects.filter(user_id__in=patient_ids)
        
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'])
    def patient_record(self, request, pk=None):
        """View a specific patient's record"""
        doctor = request.user
        patient = get_object_or_404(Patient, id=pk)
        
        # Ensure the doctor has treated this patient
        if not Appointment.objects.filter(doctor=doctor, patient=patient.user).exists():
            return Response({"error": "You are not authorized to view this patient's record"}, 
                          status=status.HTTP_403_FORBIDDEN)
        
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    @action(detail=True, methods=['POST'])
    def cancel_appointment(self, request, pk=None):
        """Cancel an appointment"""
        appointment = get_object_or_404(Appointment, id=pk, doctor=request.user)
        
        if appointment.date <= now():
            return Response({"error": "You cannot cancel past appointments"}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        appointment.status = "canceled"
        appointment.save()
        return Response({"message": "Appointment canceled successfully"}, status=status.HTTP_200_OK)
