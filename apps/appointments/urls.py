from django.urls import path, include
from . import views

urlpatterns = [
    path('appointments', views.AppointmentListView.as_view(), name='appointment.list'),
    path('appointments/<int:pk>', views.AppointmentDetailView.as_view(), name='appointment.detail'),
    path('appointments/create', views.AppointmentCreateView.as_view(), name='appointment.create'),
    path('appointments/<int:pk>/edit', views.AppointmentUpdateView.as_view(), name='appointment.edit'),
    path('appointments/<int:pk>/delete', views.AppointmentDeleteView.as_view(), name='appointment.delete'),
]