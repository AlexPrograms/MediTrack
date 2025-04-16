# from datetime import timedelta

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.utils.timezone import now

# from apps.home.decorators import role_required
# from apps.doctors.models import Doctor
# from apps.appointments.models import Appointment
# from apps.patients.models import Patient
# from django.contrib import messages
# from .forms import AppointmentForm, PatientUpdateForm

# @login_required
# @role_required("patient")
# def view_doctors(request):
#     doctors = Doctor.objects.filter(available=True)
#     return render(request, "patients_templates/view_doctors.html", {"doctors": doctors})

# @login_required
# @role_required("patient")
# def list_appointments(request):
#     appointments = Appointment.objects.filter(patient=request.user)
#     return render(request, "patients_templates/appointments.html", {"appointments": appointments})

# @login_required
# @role_required("patient")
# def create_appointment(request):
#     if request.method == "POST":
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.patient = request.user
#             appointment.save()
#             messages.success(request, "Appointment successfully created!")
#             return redirect("list_appointments")
#     else:
#         form = AppointmentForm()
#     return render(request, "patients_templates/appointment_form.html", {"form": form})

# @login_required
# @role_required("patient")
# def update_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

#     if appointment.date - now() < timedelta(hours=24):
#         messages.error(request, "You cannot edit an appointment that is within 24 hours.")
#         return redirect("list_appointments")

#     if request.method == "POST":
#         form = AppointmentForm(request.POST, instance=appointment)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Appointment updated successfully!")
#             return redirect("list_appointments")
#     else:
#         form = AppointmentForm(instance=appointment)
#     return render(request, "patients_templates/appointment_form.html", {"form": form})

# @login_required
# @role_required("patient")
# def delete_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

#     if appointment.date - now() < timedelta(hours=24):
#         messages.error(request, "You cannot delete an appointment that is within 24 hours.")
#         return redirect("list_appointments")

#     if request.method == "POST":
#         #appointment.delete() hard delete
#         appointment.status = "Cancelled"
#         appointment.save()
#         messages.success(request, "Appointment has been cancelled successfully!")
#         return redirect("list_appointments")
#     return render(request, "patients_templates/delete_appointment.html", {"appointment": appointment})

# @login_required
# @role_required("patient")
# def update_patient_details(request):
#     patient = get_object_or_404(Patient, user=request.user)
#     if request.method == "POST":
#         form = PatientUpdateForm(request.POST, instance=patient)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your health information has been updated!")
#             return redirect("update_patient_details")
#     else:
#         form = PatientUpdateForm(instance=patient)
#     return render(request, "patients_templates/update_details.html", {"form": form})
