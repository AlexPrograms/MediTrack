from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from apps.core.decorators import role_required
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import get_user_model, login

User = get_user_model()
#@method_decorator(role_required("doctor"), name="dispatch")

class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/login')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f"Welcome, {self.request.user.username}!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)


class HomeView(TemplateView):
    template_name = 'home.html'


class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    next_page = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Welcome back, {self.request.user.username}!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)



class LogoutInterfaceView(LogoutView):
    #template_name = 'logout.html'
    next_page = '/'
    #success_url = '/login'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "You have been successfully logged out.")
        return super().dispatch(request, *args, **kwargs)
