# from django.urls import reverse_lazy
#
# from .forms import AppointmentForm
# from .models import Appointment
# from django.http import Http404, HttpResponseRedirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
#from apps.home.decorators import role_required

#
# class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
#     model = Appointment
#     success_url = '/appointments'
#     template_name = 'appointments/appointment_delete.html'
#     context_object_name = 'appointment'
#
#     def get_queryset(self):
#         return Appointment.objects.filter(user=self.request.user)
#
#
# class AppointmentDetailView(LoginRequiredMixin, DetailView):
#     model = Appointment
#     template_name = 'appointments/appointment_detail.html'
#     context_object_name = 'appointment'
#
#     def get_queryset(self):
#         """Only allow users to view their own appointments."""
#         return Appointment.objects.filter(user=self.request.user)
#
#
# class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
#     model = Appointment
#     form_class = AppointmentForm
#     template_name = 'appointments/appointment_form.html'
#     context_object_name = 'appointment'
#
#     def get_queryset(self):
#         """Only allow editing appointments of the logged-in user."""
#         return Appointment.objects.filter(user=self.request.user)
#
#     def get_success_url(self):
#         """Redirect to the appointment list after saving."""
#         return reverse_lazy('appointment.list')
#
#
# class AppointmentCreateView(LoginRequiredMixin, CreateView):
#     model = Appointment
#     form_class = AppointmentForm
#     template_name = 'appointments/appointment_form.html'
#     success_url = reverse_lazy('appointment.list')
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_queryset(self):
#         """Only allow editing appointments of the logged-in user."""
#         return Appointment.objects.filter(user=self.request.user)
#
#
# class AppointmentListView(LoginRequiredMixin, ListView):
#     model = Appointment
#     context_object_name = 'appointments'
#     template_name = 'appointments/appointment_list.html'
#     login_url = '/admin'
#
#     def get_queryset(self):
#         return Appointment.objects.filter(user=self.request.user)
