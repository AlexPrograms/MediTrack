# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render
#from apps.home.decorators import role_required

#
# def patient_check(user):
#     return user.is_authenticated and user.role == "patient"
#
# @user_passes_test(patient_check)
# def patient_dashboard(request):
#     return render(request, "patients/dashboard.html")
