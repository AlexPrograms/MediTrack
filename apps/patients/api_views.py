from rest_framework.viewsets import ModelViewSet
from apps.home.permissions import IsPatient  # Import custom permission
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsPatient]  # Only patients can access
