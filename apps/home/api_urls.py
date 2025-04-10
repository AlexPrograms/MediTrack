from django.urls import path
from .api_views import SignUpAPIView, login_api, LogoutAPIView, HomeAPIView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup_api'),
    path('login/', login_api, name='login_api'),
    path('logout/', LogoutAPIView.as_view(), name='logout_api'),
    path('home/', HomeAPIView.as_view(), name='home_api'),
]
