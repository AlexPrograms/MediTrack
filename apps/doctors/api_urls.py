from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import DoctorViewSet

router = DefaultRouter()
router.register(r'', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]