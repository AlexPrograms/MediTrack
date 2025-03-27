from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'get_patient', 'get_doctor')  # Change 'user' to 'get_user'
    list_filter = ('date',)  # Remove 'user' if it's not a valid field

    def get_patient(self, obj):
        return obj.patient.username if obj.patient else "No Patient"
    get_patient.admin_order_field = 'patient'
    get_patient.short_description = 'Patient'

    def get_doctor(self, obj):
        return obj.doctor.username if obj.doctor else "No Doctor"
    get_doctor.admin_order_field = 'doctor'
    get_doctor.short_description = 'Doctor'

admin.site.register(Appointment, AppointmentAdmin)
