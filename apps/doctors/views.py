from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.utils.timezone import now

from apps.appointments.models import Appointment
from apps.patients.models import Patient
from apps.home.decorators import role_required


@login_required
@role_required("doctor")
def view_appointments(request):
    doctor = request.user
    sort_by = request.GET.get("sort", "date")  # Sorting logic
    if sort_by == "patient":
        appointments = Appointment.objects.filter(doctor=doctor).order_by("patient__last_name")
    else:
        appointments = Appointment.objects.filter(doctor=doctor).order_by("date")

    return render(request, "doctors_templates/view_appointments.html", {"appointments": appointments})


@login_required
@role_required("doctor")
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)

    if appointment.date <= now():
        messages.error(request, "You cannot cancel past appointments.")
        return redirect("view_appointments")

    if request.method == "POST":
        appointment.status = "canceled"
        appointment.save()
        messages.success(request, "Appointment canceled successfully.")
        return redirect("view_appointments")

    return render(request, "doctors_templates/cancel_appointment.html", {"appointment": appointment})


@login_required
@role_required("doctor")
def view_patients(request):
    doctor = request.user
    patient_ids = Appointment.objects.filter(doctor=doctor).values_list("patient", flat=True).distinct()
    patients = Patient.objects.filter(user_id__in=patient_ids)

    return render(request, "doctors_templates/view_patients.html", {"patients": patients})


@login_required
@role_required("doctor")
def view_patient_record(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    # Ensure the doctor has treated this patient
    if not Appointment.objects.filter(doctor=request.user, patient=patient.user).exists():
        messages.error(request, "You are not authorized to view this patient's record.")
        return redirect("view_patients")

    return render(request, "doctors_templates/patient_record.html", {"patient": patient})
