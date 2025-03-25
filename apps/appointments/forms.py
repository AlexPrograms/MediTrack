from django.utils.timezone import is_naive, now, make_aware, get_current_timezone

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['title', 'description', 'date']

    def clean_date(self):
        appointment_date = self.cleaned_data.get('date')

        if appointment_date:
            # Make the date timezone-aware only if it is naive
            if is_naive(appointment_date):
                appointment_date = make_aware(appointment_date, get_current_timezone())

            # Get the current timezone-aware datetime
            current_time = now()

            # Validate the date
            if appointment_date < current_time:
                raise forms.ValidationError("The appointment date cannot be in the past.")

        return appointment_date