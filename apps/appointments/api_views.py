# apps/appointments/api_views.py
from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment
from .serializers import AppointmentSerializer
from apps.home.permissions import IsDoctor, IsPatient
from datetime import timedelta
from django.utils.timezone import now


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing appointments.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'date']
    search_fields = ['doctor__user__username', 'patient__username', 'notes']
    ordering_fields = ['date', 'status']

    def get_queryset(self):
        """
        Filter appointments based on the logged-in user's role.
        """
        user = self.request.user
        if user.is_doctor:
            return Appointment.objects.filter(doctor=user)
        elif user.is_patient:
            return Appointment.objects.filter(patient=user)
        return Appointment.objects.none()

    def perform_create(self, serializer):
        """
        Overriding to assign the logged-in user as the patient when creating an appointment.
        """
        user = self.request.user
        serializer.save(patient=user)

    @action(detail=True, methods=['post'], permission_classes=[IsPatient])
    def cancel(self, request, pk=None):
        """
        Custom action to cancel an appointment (soft delete).
        """
        appointment = self.get_object()

        if appointment.patient != request.user:
            return Response({"error": "You are not the patient for this appointment."}, status=status.HTTP_403_FORBIDDEN)

        # Prevent cancellation if appointment is within 24 hours
        if appointment.date - now() < timedelta(hours=24):
            return Response({"error": "Cannot cancel appointment within 24 hours."}, status=status.HTTP_400_BAD_REQUEST)

        appointment.status = "Cancelled"
        appointment.save()
        return Response({"message": "Appointment successfully cancelled."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsPatient])
    def reschedule(self, request, pk=None):
        """
        Custom action to reschedule an appointment (update date).
        """
        appointment = self.get_object()

        if appointment.patient != request.user:
            return Response({"error": "You are not the patient for this appointment."}, status=status.HTTP_403_FORBIDDEN)

        # Prevent rescheduling if appointment is within 24 hours
        if appointment.date - now() < timedelta(hours=24):
            return Response({"error": "Cannot reschedule appointment within 24 hours."}, status=status.HTTP_400_BAD_REQUEST)

        new_date = request.data.get('new_date')
        appointment.date = new_date
        appointment.save()

        return Response({"message": "Appointment successfully rescheduled."}, status=status.HTTP_200_OK)
