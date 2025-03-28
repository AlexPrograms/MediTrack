from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.utils.timezone import now

from apps.appointments.models import Appointment
from apps.patients.models import Patient
from apps.home.decorators import role_required
from apps.appointments.utils import bubble_sort, quick_sort, filter_appointments


@login_required
@role_required("doctor")
def view_appointments(request):
    doctor = request.user
    sort_by = request.GET.get("sort", "date")
    #filter_status = request.GET.get("status", "all")
    # default sorting logic, used previously
    # if sort_by == "patient":
    #     appointments = Appointment.objects.filter(doctor=doctor).order_by("patient__last_name")
    # else:
    #     appointments = Appointment.objects.filter(doctor=doctor).order_by("date")
    # custom sorting logic with quick and bubble sorts
    filter_status = request.GET.get("status", None)
    algorithm = request.GET.get("algo", "quick")  # change to choose different algo

    appointments = list(Appointment.objects.filter(doctor=doctor))

    # if filter_status == "scheduled":
    #     appointments = appointments.filter(status="scheduled")
    # elif filter_status == "completed":
    #     appointments = appointments.filter(Q(status="completed") | Q(date__lt=now(), ~Q(status="canceled")))
    # elif filter_status == "canceled":
    #     appointments = appointments.filter(status="canceled")
    #appointments = filter_appointments(appointments, status=filter_status)


    if filter_status:
        appointments = filter_appointments(appointments, status=filter_status)

    if sort_by == "patient":
        key_func = lambda x: x.patient.first_name.lower()
    else:
        key_func = lambda x: x.date

    # Use selected sorting algorithm
    if algorithm == "bubble":
        appointments = bubble_sort(appointments, key_func)
    else:
        appointments = quick_sort(appointments, key_func)

    return render(request, "doctors_templates/view_appointments.html", {"appointments": appointments})


@login_required
@role_required("doctor")
def filter_appointments(appointments, status=None):
    """Filters appointments based on status."""
    if status and status in dict(Appointment.STATUS_CHOICES):
        return appointments.filter(status=status)
    return appointments


from collections import Counter


@login_required
@role_required("doctor")
def most_frequent_patient(request):
    doctor = request.user
    appointments = Appointment.objects.filter(doctor=doctor)

    patient_counts = Counter(a.patient for a in appointments)
    if not patient_counts:
        patients = None
    else:
        max_count = max(patient_counts.values())
        patients = [(patient, count) for patient, count in patient_counts.items() if count == max_count]

    return render(request, "doctors_templates/most_frequent_patient.html", {"patients": patients})



@login_required
@role_required("doctor")
def search_patient_appointments(request):
    doctor = request.user
    query = request.GET.get("q", "").strip().lower()
    appointments = list(Appointment.objects.filter(doctor=doctor))

    if query:
        found_appointments = [a for a in appointments if query in a.patient.username.lower() or query in a.patient.first_name.lower()]
    else:
        found_appointments = appointments

    return render(request, "doctors_templates/view_appointments.html", {"appointments": found_appointments})


@login_required
@role_required("doctor")
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)

    if appointment.date <= now():
        messages.error(request, "You cannot cancel past appointments.")
        return redirect("view_appointments")

    if request.method == "POST":
        appointment.status = "canceled"
        appointment.delete()
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
