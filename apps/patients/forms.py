from django import forms
from apps.appointments.models import Appointment
from apps.patients.models import Patient
from apps.doctors.models import Doctor

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
        self.fields["doctor"].queryset = Doctor.objects.filter(available=True)
        self.fields["doctor"].widget.attrs.update({"class": "form-control"})

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["date_of_birth", "age", "gender", "medical_history", "current_condition"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "medical_history": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "current_condition": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
