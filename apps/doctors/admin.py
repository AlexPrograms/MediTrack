from django.contrib import admin
from .models import Doctor
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user", "specialization", "phone", "experience_years", "available")
    search_fields = ("user__first_name", "user__last_name", "specialization")
    list_filter = ("specialization", "available")
    ordering = ("user__first_name",)

