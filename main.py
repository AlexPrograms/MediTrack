from models import User, Doctor, Patient, Appointment, MedicalRecord
from methods import HomeApp, DoctorsApp, PatientsApp, AppointmentsApp
from datetime import datetime, date
import time

def print_separator(title):
    print("\n" + "=" * 50)
    print(f" {title} ".center(50, "="))
    print("=" * 50)

# -------- HomeApp Functionality Demo --------
print_separator("HomeApp Functionality Demo")

# Create sample users
users = []
admin_user = User("admin1", "admin@example.com", "securepass", "Alice", "Admin", "admin")
doctor_user1 = User("doctorJohn", "john@example.com", "docpass", "John", "Smith", "doctor")
doctor_user2 = User("doctorSarah", "sarah@example.com", "docpass2", "Sarah", "Johnson", "doctor")
patient_user1 = User("patientJane", "jane@example.com", "patpass", "Jane", "Doe", "patient")
patient_user2 = User("patientMike", "mike@example.com", "patpass2", "Mike", "Wilson", "patient")

# Register users
print("Registering users...")
for user in [admin_user, doctor_user1, doctor_user2, patient_user1, patient_user2]:
    HomeApp.register(users, user)
    print(f"Registered {user.username} ({user.role})")

# Authentication and login
print("\nTesting authentication:")
print(f"Admin auth: {HomeApp.authenticate(admin_user, 'securepass')}")
print(f"Doctor auth with wrong password: {HomeApp.authenticate(doctor_user1, 'wrongpass')}")

print("\nTesting login:")
print(HomeApp.login(patient_user1, "patpass"))
print(HomeApp.login(doctor_user2, "wrongpass"))

# Logout
print("\nTesting logout:")
print(HomeApp.logout(admin_user))

# Manage users
print("\nManaging users:")
for user_info in HomeApp.manage_users(users):
    print(user_info)

# -------- Create Profiles --------
print_separator("Creating Doctor and Patient Profiles")

# Create doctor profiles
doctor1 = Doctor(doctor_user1, "Cardiology", "123-456-7890", 10)
doctor2 = Doctor(doctor_user2, "Neurology", "987-654-3210", 15)
doctors = [doctor1, doctor2]

print(f"Created doctor: {doctor1.user.first_name} {doctor1.user.last_name}, {doctor1.specialization}")
print(f"Created doctor: {doctor2.user.first_name} {doctor2.user.last_name}, {doctor2.specialization}")

# Create patient profiles
patient1 = Patient(
    patient_user1, 
    date(1990, 5, 20), 
    34, 
    "female", 
    medical_history="Asthma since childhood",
    current_condition="Mild seasonal allergies",
    allergies="Pollen, dust",
    medications="Albuterol inhaler",
    blood_type="A+", 
    weight=65, 
    height=165,
    blood_pressure="120/80 mmHg",
    heart_rate=72,
    cholesterol_level=180.5,
    glucose_level=95.2
)

patient2 = Patient(
    patient_user2, 
    date(1985, 8, 15), 
    40, 
    "male", 
    medical_history="Fractured right arm in 2018",
    current_condition="Hypertension",
    allergies="Penicillin",
    medications="Lisinopril 10mg daily",
    blood_type="O+", 
    weight=82, 
    height=178,
    blood_pressure="140/90 mmHg",
    heart_rate=68,
    cholesterol_level=210.3,
    glucose_level=105.7
)

patients = [patient1, patient2]

print(f"\nCreated patient: {patient1.user.first_name} {patient1.user.last_name}, Age: {patient1.age}")
print(f"Created patient: {patient2.user.first_name} {patient2.user.last_name}, Age: {patient2.age}")

# -------- PatientsApp Functionality Demo --------
print_separator("PatientsApp Functionality Demo")

# View available doctors
print("Available doctors:")
for doc in PatientsApp.view_doctors(doctors):
    print(f"Dr. {doc.user.first_name} {doc.user.last_name}, {doc.specialization}")

# Create appointments
print("\nCreating appointments...")
appt1 = PatientsApp.create_appointment(
    doctor1, patient1, "Regular checkup", 
    datetime(2025, 4, 20, 10, 0), "Annual physical"
)

appt2 = PatientsApp.create_appointment(
    doctor1, patient1, "Follow-up", 
    datetime(2025, 4, 25, 14, 30), "Review test results"
)

appt3 = PatientsApp.create_appointment(
    doctor2, patient2, "Initial consultation", 
    datetime(2025, 4, 22, 9, 15), "Headache evaluation"
)

appt4 = PatientsApp.create_appointment(
    doctor1, patient2, "Consultation", 
    datetime(2025, 4, 30, 11, 0), "Heart palpitations"
)

appointments = [appt1, appt2, appt3, appt4]

print(f"Created {len(appointments)} appointments")

# Update appointment
print("\nUpdating appointment...")
updated_appt = PatientsApp.update_appointment(
    appt1, 
    description="Comprehensive physical exam", 
    date=datetime(2025, 4, 21, 11, 0)
)
print(f"Updated appointment to: {updated_appt.description} on {updated_appt.date}")

# Update health details
print("\nUpdating patient health details...")
updated_patient = PatientsApp.update_health_details(
    patient1,
    weight=67.5,
    blood_pressure="118/78 mmHg",
    heart_rate=70
)
print(f"Updated {updated_patient.user.first_name}'s health details:")
print(f"Weight: {updated_patient.weight}, BP: {updated_patient.blood_pressure}, HR: {updated_patient.heart_rate}")

# Create medical records
print("\nCreating medical records...")
record1 = MedicalRecord(
    patient1, doctor1,
    "Mild hypertension",
    "Lisinopril 5mg daily, reduce sodium intake",
    datetime(2025, 4, 1),
    "Follow up in 3 months"
)

record2 = MedicalRecord(
    patient1, doctor1,
    "Seasonal allergies",
    "Cetirizine 10mg daily as needed",
    datetime(2025, 3, 15),
    "Symptoms well controlled"
)

record3 = MedicalRecord(
    patient2, doctor2,
    "Tension headaches",
    "Ibuprofen 400mg as needed, stress management techniques",
    datetime(2025, 3, 20),
    "Likely stress-related"
)

print(f"Created {len(patient1.medical_records)} medical records for {patient1.user.first_name}")
print(f"Created {len(patient2.medical_records)} medical record for {patient2.user.first_name}")

# View medical records
print("\nViewing medical records for Jane:")
for record in PatientsApp.view_medical_records(patient1):
    print(f"Date: {record.visit_date.date()}, Diagnosis: {record.diagnosis}, Prescription: {record.prescription}")

# Delete appointment
print("\nDeleting appointment...")
print(PatientsApp.delete_appointment(appt2, doctor1, patient1))

# -------- DoctorsApp Functionality Demo --------
print_separator("DoctorsApp Functionality Demo")

# View appointments for a doctor
print(f"Dr. {doctor1.user.last_name}'s appointments:")
for appt in DoctorsApp.view_appointments(doctor1):
    print(f"Patient: {appt.patient.user.first_name} {appt.patient.user.last_name}, Date: {appt.date}, Status: {appt.status}")

# Cancel appointment
print("\nCanceling appointment...")
print(DoctorsApp.cancel_appointment(appt1))

# View patients
print("\nDr. Smith's patients:")
for pat in DoctorsApp.view_patients(doctor1):
    print(f"{pat.user.first_name} {pat.user.last_name}, Age: {pat.age}")

# View patient record
print("\nViewing Jane's medical records:")
for record in DoctorsApp.view_patient_record(patient1):
    print(f"Date: {record.visit_date.date()}, Diagnosis: {record.diagnosis}")

# Sort appointments
print("\nSorting appointments by date:")
for appt in DoctorsApp.sort_appointments(doctor1.appointments, by='date'):
    print(f"Date: {appt.date}, Patient: {appt.patient.user.last_name}")

print("\nSorting appointments by patient:")
for appt in DoctorsApp.sort_appointments(doctor1.appointments, by='patient'):
    print(f"Patient: {appt.patient.user.last_name}, Date: {appt.date}")

# Filter appointments
print("\nFiltering appointments by status:")
for appt in DoctorsApp.filter_appointments(doctor1.appointments, status='canceled'):
    print(f"Canceled appointment: {appt.patient.user.last_name}, {appt.date}")

# Most frequent patient
print("\nMost frequent patient:")
freq_patient = DoctorsApp.most_frequent_patient(doctor1)
if freq_patient:
    print(f"{freq_patient.user.first_name} {freq_patient.user.last_name}")
else:
    print("No frequent patient found")

# Search patient appointments
print("\nSearching for Jane's appointments:")
for appt in DoctorsApp.search_patient_appointments(doctor1.appointments, "Jane"):
    print(f"Found: {appt.date}, {appt.description}, Status: {appt.status}")

# -------- AppointmentsApp Functionality Demo --------
print_separator("AppointmentsApp Functionality Demo")

# List all appointments
print("All appointments:")
for appt in AppointmentsApp.list_appointments(appointments):
    print(f"Doctor: {appt.doctor.user.last_name}, Patient: {appt.patient.user.last_name}, Date: {appt.date}, Status: {appt.status}")

# Filter appointments
print("\nScheduled appointments:")
for appt in AppointmentsApp.filter_appointments(appointments, 'scheduled'):
    print(f"Doctor: {appt.doctor.user.last_name}, Patient: {appt.patient.user.last_name}, Date: {appt.date}")

# Search patient appointments
print("\nSearching for Mike's appointments:")
for appt in AppointmentsApp.search_patient_appointments(appointments, "Mike"):
    print(f"Found: Dr. {appt.doctor.user.last_name}, {appt.date}, {appt.description}")
