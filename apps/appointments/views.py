from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer
from apps.core.permissions import IsDoctor, IsPatient, IsOwnerOrAdmin

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsPatient]  # Only patients can create appointments
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        # Doctors see their appointments
        if hasattr(self.request.user, 'doctor'):
            return Appointment.objects.filter(doctor=self.request.user.doctor)
        # Patients see their appointments
        elif hasattr(self.request.user, 'patient'):
            return Appointment.objects.filter(patient=self.request.user.patient)
        # Admin sees all
        elif self.request.user.is_staff:
            return Appointment.objects.all()
        return Appointment.objects.none()

    @action(detail=True, methods=['patch'])
    def approve(self, request, pk=None):
        appointment = self.get_object()
        if appointment.status in ['cancelled', 'completed']:
            return Response({"detail": "You cannot approve a cancelled or completed appointment."},
                          status=status.HTTP_400_BAD_REQUEST)
        if request.user.doctor != appointment.doctor:
            return Response({"detail": "Only the assigned doctor can approve appointments."},
                          status=status.HTTP_403_FORBIDDEN)
        appointment.status = 'approved'
        appointment.save()
        return Response(self.get_serializer(appointment).data)

    @action(detail=True, methods=['patch'])
    def cancel(self, request, pk=None):
        appointment = self.get_object()
        if appointment.status == 'completed':
            return Response({"detail": "You cannot cancel a completed appointment."},
                          status=status.HTTP_400_BAD_REQUEST)
        if hasattr(request.user, 'doctor') and request.user.doctor == appointment.doctor:
            appointment.status = 'cancelled'
        elif hasattr(request.user, 'patient') and request.user.patient == appointment.patient:
            appointment.status = 'cancelled'
        else:
            return Response({"detail": "Only the assigned doctor or patient can cancel appointments."},
                          status=status.HTTP_403_FORBIDDEN)
        appointment.save()
        return Response(self.get_serializer(appointment).data)
