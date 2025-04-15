"""
URL configuration for MediTrack project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MediTrack API",
        default_version='v1',
        description="API documentation for MediTrack application",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    # path('', include('apps.doctors.urls')),
    # path('', include('apps.patients.urls')),
    # path('', include('apps.appointments.urls')),

    # API Routes
    path('api/doctors/', include('apps.doctors.api_urls')),
    path('api/patients/', include('apps.patients.api_urls')),
    path('api/appointments/', include('apps.appointments.api_urls')),
    path('api/auth/', include('apps.home.api_urls')),
    path('api-auth/', include('rest_framework.urls')),

    #Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
