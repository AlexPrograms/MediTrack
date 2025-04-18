from datetime import timedelta

from django import forms
from django.utils.timezone import now

from apps.appointments.models import Appointment
from apps.patients.models import Patient
from apps.doctors.models import Doctor
from apps.core.models import User

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "date", "reason", "description"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "reason": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields["doctor"].queryset = User.objects.filter(role="doctor", doctor__available=True)
        self.fields["doctor"].label_from_instance = lambda \
            obj: f"{obj.username} {obj.last_name} - {obj.doctor.specialization}"
        self.fields["doctor"].widget.attrs.update({"class": "form-control"})

    def clean_date(self):
        appointment_date = self.cleaned_data.get("date")
        if appointment_date and appointment_date <= now() + timedelta(hours=5):
            raise forms.ValidationError("You cannot create an appointment in the past "
                                        "or too close to your current time")
        return appointment_date

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "date_of_birth",
            "age",
            "gender",
            "medical_history",
            "current_condition",
            "allergies",
            "medications",
            "blood_type",
            "weight",
            "height",
            "blood_pressure",
            "heart_rate",
            "cholesterol_level",
            "glucose_level",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "medical_history": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Past illnesses, treatments, surgeries..."}),
            "current_condition": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Describe ongoing health conditions..."}),
            "allergies": forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "List any allergies..."}),
            "medications": forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "List any current medications..."}),
            "blood_type": forms.Select(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control", "step": "0.1", "placeholder": "Weight in kg"}),
            "height": forms.NumberInput(attrs={"class": "form-control", "step": "0.1", "placeholder": "Height in cm"}),
            "blood_pressure": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g., 120/80 mmHg"}),
            "heart_rate": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Beats per minute"}),
            "cholesterol_level": forms.NumberInput(attrs={"class": "form-control", "step": "0.1", "placeholder": "mg/dL"}),
            "glucose_level": forms.NumberInput(attrs={"class": "form-control", "step": "0.1", "placeholder": "mg/dL"}),
        }