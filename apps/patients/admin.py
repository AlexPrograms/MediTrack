from django.contrib import admin
from .models import Patient
# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_birth", "age", "gender", "blood_type")
    search_fields = ("user__first_name", "user__last_name")
    list_filter = ("gender", "blood_type")
    ordering = ("user__first_name",)

