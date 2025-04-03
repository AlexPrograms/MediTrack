# MediTrack - Medical Appointment Management System

## 📌 Overview

MediTrack is a medical appointment and patient management system designed to streamline doctor-patient interactions. It allows doctors to manage appointments, view patient records, and track medical history, while patients can book and manage their appointments and update personal health details.

## 🚀 Features

### 🔐 User Authentication & Role Management
- **Custom User Model** with roles:
  - **Admin**: Manages users.
  - **Doctor**: Manages appointments and patients.
  - **Patient**: Books and manages appointments.
- **Authentication System**: Login, logout, registration.
- **Role-Based Access Control**: Views restricted based on user roles.

### 👨‍⚕️ Doctor Features
- View upcoming and past appointments.
- Sort appointments by date or patient name (**Quick Sort, Bubble Sort**).
- Filter appointments (**Canceled, Past, Upcoming, All**).
- Cancel appointments.
- View assigned patients.
- Access patient medical records (**history, allergies, medications, vitals**).

### 🩺 Patient Features
- View available doctors.
- Book, update, delete appointments.
- Update personal health details (**allergies, medications, vitals, medical history**).

### 📊 Algorithms
- **Sorting Algorithms**: Quick Sort, Bubble Sort for appointments.
- **Filtering**: Filter appointments by status.
- **Find Most Frequent Patient** based on appointment count.
- **Search for Patient Appointments**.

## 🏗️ Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, Bootstrap
- **Database**: SQLite (can be replaced with PostgreSQL/MySQL)
- **Authentication**: Django Custom User Model

## 🔧 Installation

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/yourusername/meditrack.git
$ cd meditrack
```

### 2️⃣ Create and Activate Virtual Environment
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

### 4️⃣ Apply Migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### 5️⃣ Create Superuser (Admin Access)
```sh
$ python manage.py createsuperuser
```

### 6️⃣ Run the Server
```sh
$ python manage.py runserver
```

## 📂 Project Structure
```
meditrack/
│── apps/
│   ├── home/           # Authentication & User Management
│   ├── appointments/   # Appointment Management
│   ├── doctors/        # Doctor Management
│   ├── patients/       # Patient Management
│── templates/          # Frontend HTML Templates
│── static/             # CSS, JS, Images
│── manage.py           # Django Management Script
```

## 🛠️ Future Improvements
- Implement **notifications/reminders** for appointments.
- Improve **search functionality** for doctors & patients.
- Add **exportable reports** (PDF, Excel) for medical records.


## 📬 Contact
For any inquiries, reach out to `prohunter872@gmail.com` 