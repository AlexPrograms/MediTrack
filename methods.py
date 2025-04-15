from datetime import datetime
from collections import Counter
from models import Appointment, MedicalRecord


class HomeApp:
    @staticmethod
    def authenticate(user, password):
        return user.password == password

    @staticmethod
    def register(user_list, new_user):
        user_list.append(new_user)
        return new_user

    @staticmethod
    def login(user, password):
        if HomeApp.authenticate(user, password):
            return f"Login successful for {user.username}"
        return "Invalid credentials"

    @staticmethod
    def logout(user):
        return f"{user.username} has been logged out."

    @staticmethod
    def manage_users(users):
        return [f"{user.username} ({user.role})" for user in users]



class DoctorsApp:
    @staticmethod
    def view_appointments(doctor):
        return doctor.appointments

    @staticmethod
    def cancel_appointment(appointment):
        appointment.status = 'canceled'
        appointment.updated_at = datetime.now()
        return f"Appointment {appointment.id} has been canceled."

    @staticmethod
    def view_patients(doctor):
        # Use a set to remove duplicates if a patient has multiple appointments
        return list({appt.patient for appt in doctor.appointments})

    @staticmethod
    def view_patient_record(patient):
        return patient.medical_records

    @staticmethod
    def sort_appointments(appointments, by='date'):
        if by == 'patient':
            return sorted(appointments, key=lambda a: a.patient.user.last_name)
        return sorted(appointments, key=lambda a: a.date)

    @staticmethod
    def filter_appointments(appointments, status='scheduled'):
        return [appt for appt in appointments if appt.status == status]

    @staticmethod
    def most_frequent_patient(doctor):
        patient_ids = [appt.patient.user.id for appt in doctor.appointments]
        if not patient_ids:
            return None
        most_common_id = Counter(patient_ids).most_common(1)[0][0]
        for appt in doctor.appointments:
            if appt.patient.user.id == most_common_id:
                return appt.patient
        return None

    @staticmethod
    def search_patient_appointments(appointments, patient_name):
        return [
            appt for appt in appointments
            if patient_name.lower() in appt.patient.user.first_name.lower()
            or patient_name.lower() in appt.patient.user.last_name.lower()
        ]



class PatientsApp:
    @staticmethod
    def view_doctors(doctors_list):
        return [doctor for doctor in doctors_list if doctor.available]

    @staticmethod
    def create_appointment(doctor, patient, description, date, reason):
        return Appointment(doctor, patient, description, date, reason)

    @staticmethod
    def update_appointment(appointment, description=None, date=None, reason=None):
        if description:
            appointment.description = description
        if date:
            appointment.date = date
        if reason:
            appointment.reason = reason
        appointment.updated_at = datetime.now()
        return appointment

    @staticmethod
    def delete_appointment(appointment, doctor, patient):
        if appointment in doctor.appointments:
            doctor.appointments.remove(appointment)
        if appointment in patient.appointments:
            patient.appointments.remove(appointment)
        return f"Appointment {appointment.id} deleted."

    @staticmethod
    def update_health_details(patient, **kwargs):
        for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        return patient

    @staticmethod
    def view_medical_records(patient):
        return patient.medical_records



class AppointmentsApp:
    @staticmethod
    def list_appointments(appointments):
        return appointments

    @staticmethod
    def filter_appointments(appointments, status):
        return [appt for appt in appointments if appt.status == status]

    @staticmethod
    def search_patient_appointments(appointments, patient_name):
        # Reusing the same logic as in DoctorsApp
        return DoctorsApp.search_patient_appointments(appointments, patient_name)
