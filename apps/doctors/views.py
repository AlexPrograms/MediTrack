from django.shortcuts import render
from apps.home.decorators import role_required

# Create your views here.
# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render
#
# def doctor_check(user):
#     return user.is_authenticated and user.role == "doctor"
#
# @user_passes_test(doctor_check)
# def doctor_dashboard(request):
#     return render(request, "doctors/dashboard.html")
