from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/appointments'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/login')
        return super().get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'


class LoginInterfaceView(LoginView):
    template_name = 'login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

