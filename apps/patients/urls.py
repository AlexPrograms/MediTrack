from django.urls import path, include
from . import views

urlpatterns = [
    path("doctors/", views.view_doctors, name="patients_templates"),
    path("appointments/", views.list_appointments, name="list_appointments"),
    path("appointments/create/", views.create_appointment, name="create_appointment"),
    path("appointments/update/<int:appointment_id>/", views.update_appointment, name="update_appointment"),
    path("appointments/delete/<int:appointment_id>/", views.delete_appointment, name="delete_appointment"),
    path("update-details/", views.update_patient_details, name="update_patient_details"),
]