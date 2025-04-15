from uuid import uuid4
from datetime import datetime, date


class User:
    def __init__(self, username, email, password, first_name, last_name, role='patient'):
        self.id = uuid4()
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = role  # "admin", "doctor", "patient"
        self.date_joined = datetime.now()
        self.is_active = True

    def is_admin(self):
        return self.role == 'admin'

    def is_doctor(self):
        return self.role == 'doctor'

    def is_patient(self):
        return self.role == 'patient'



class Doctor:
    def __init__(self, user, specialization, phone, experience_years, available=True):
        self.user = user  # OneToOne User
        self.specialization = specialization
        self.phone = phone
        self.experience_years = experience_years
        self.available = available
        self.appointments = []
        self.medical_records = []




class Patient:
    def __init__(self, user, date_of_birth, age, gender, medical_history='', current_condition='',
                 allergies='', medications='', blood_type='', weight=0.0, height=0.0,
                 blood_pressure='', heart_rate=0, cholesterol_level=0.0, glucose_level=0.0):
        self.user = user  # OneToOne User
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender  
        self.medical_history = medical_history
        self.current_condition = current_condition
        self.allergies = allergies
        self.medications = medications
        self.blood_type = blood_type
        self.weight = weight
        self.height = height
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.cholesterol_level = cholesterol_level
        self.glucose_level = glucose_level
        self.appointments = []
        self.medical_records = []




class Appointment:
    def __init__(self, doctor, patient, description, date, reason, status='scheduled'):
        self.id = uuid4()
        self.doctor = doctor
        self.patient = patient  
        self.description = description
        self.date = date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reason = reason
        self.status = status
        # Link the appointment
        doctor.appointments.append(self)
        patient.appointments.append(self)

    def dynamic_status(self):
        if self.status != 'scheduled':
            return self.status
        return 'missed' if datetime.now() > self.date else self.status


class MedicalRecord:
    def __init__(self, patient, doctor, diagnosis, prescription, visit_date, notes=''):
        self.id = uuid4()
        self.patient = patient
        self.doctor = doctor
        self.diagnosis = diagnosis
        self.prescription = prescription
        self.visit_date = visit_date
        self.notes = notes
        # Link to patient and doctor
        patient.medical_records.append(self)
        doctor.medical_records.append(self)


