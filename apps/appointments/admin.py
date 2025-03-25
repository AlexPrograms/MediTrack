from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'get_user')  # Change 'user' to 'get_user'
    list_filter = ('date',)  # Remove 'user' if it's not a valid field

    def get_user(self, obj):
        return obj.user.username if obj.user else "No User"
    get_user.admin_order_field = 'user'  # Allows sorting by user
    get_user.short_description = 'User'  # Display name in the admin

admin.site.register(Appointment, AppointmentAdmin)
