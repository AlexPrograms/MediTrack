from django.urls import path, include
from . import views

urlpatterns = [
    path("appointments_doctor/", views.view_appointments, name="view_appointments"),
    path("appointments_doctor/cancel/<int:appointment_id>/", views.cancel_appointment, name="cancel_appointment"),
    path("patients/", views.view_patients, name="view_patients"),
    path("patients/<int:patient_id>/", views.view_patient_record, name="view_patient_record"),
]