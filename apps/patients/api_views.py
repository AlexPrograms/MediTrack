from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from datetime import timedelta

from apps.home.permissions import IsPatient  # Import custom permission
from .models import Patient
from .serializers import PatientSerializer
from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorSerializer
from apps.appointments.models import Appointment
from apps.appointments.serializers import AppointmentSerializer

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsPatient]  # Only patients can access
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'blood_type']
    ordering_fields = ['name', 'date_of_birth']
    
    @action(detail=False, methods=['GET'])
    def doctors(self, request):
        """Get all available doctors"""
        doctors = Doctor.objects.filter(available=True)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def appointments(self, request):
        """Get all appointments for the logged-in patient"""
        appointments = Appointment.objects.filter(patient=request.user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'])
    def create_appointment(self, request):
        """Create a new appointment"""
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_appointment(self, request, pk=None):
        """Update an existing appointment"""
        appointment = get_object_or_404(Appointment, id=pk, patient=request.user)
        
        # Check if appointment is within 24 hours
        if appointment.date - now() < timedelta(hours=24):
            return Response({"error": "You cannot edit an appointment that is within 24 hours"}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['DELETE'])
    def cancel_appointment(self, request, pk=None):
        """Cancel/delete an appointment"""
        appointment = get_object_or_404(Appointment, id=pk, patient=request.user)
        
        # Check if appointment is within 24 hours
        if appointment.date - now() < timedelta(hours=24):
            return Response({"error": "You cannot cancel an appointment that is within 24 hours"}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        # Soft delete by changing status
        appointment.status = "Cancelled"
        appointment.save()
        return Response({"message": "Appointment has been cancelled successfully"}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['PUT', 'PATCH'])
    def update_details(self, request):
        """Update patient health information"""
        patient = get_object_or_404(Patient, user=request.user)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
