from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import PatientViewSet

router = DefaultRouter()
router.register(r'', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Add custom API endpoints here
]