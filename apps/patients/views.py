from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.home.decorators import role_required
from apps.doctors.models import Doctor
from apps.appointments.models import Appointment
from apps.patients.models import Patient
from django.contrib import messages
from .forms import AppointmentForm, PatientUpdateForm

@login_required
@role_required("patient")
def view_doctors(request):
    doctors = Doctor.objects.filter(available=True)
    return render(request, "view_doctors.html", {"doctors": doctors})

@login_required
@role_required("patient")
def list_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, "appointments.html", {"appointments": appointments})

@login_required
@role_required("patient")
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            messages.success(request, "Appointment successfully created!")
            return redirect("list_appointments")
    else:
        form = AppointmentForm()
    return render(request, "appointment_form.html", {"form": form})

@login_required
@role_required("patient")
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully!")
            return redirect("list_appointments")
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, "appointment_form.html", {"form": form})

@login_required
@role_required("patient")
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)
    if request.method == "POST":
        appointment.delete()
        messages.success(request, "Appointment deleted successfully!")
        return redirect("list_appointments")
    return render(request, "delete_appointment.html", {"appointment": appointment})

@login_required
@role_required("patient")
def update_patient_details(request):
    patient = get_object_or_404(Patient, user=request.user)
    if request.method == "POST":
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Your health information has been updated!")
            return redirect("update_patient_details")
    else:
        form = PatientUpdateForm(instance=patient)
    return render(request, "update_details.html", {"form": form})
