from django.shortcuts import render
from django.http import HttpResponseForbidden
from functools import wraps

def role_required(role):
    """Decorator to restrict views based on user role"""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator

