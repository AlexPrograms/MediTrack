from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AppointmentViewSet

router = DefaultRouter()
router.register(r'', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add custom API endpoints here
]