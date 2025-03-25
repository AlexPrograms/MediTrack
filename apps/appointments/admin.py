from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('date', 'user')
