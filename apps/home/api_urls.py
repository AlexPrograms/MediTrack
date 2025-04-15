from django.urls import path, include
# from .api_views import SignUpAPIView, login_api, LogoutAPIView, HomeAPIView
from .api_views import register_user, login_user, LogoutAPIView

# urlpatterns = [
#     path('signup/', SignUpAPIView.as_view(), name='signup_api'),
#     path('login/', login_api, name='login_api'),
#     path('logout/', LogoutAPIView.as_view(), name='logout_api'),
#     #path('home/', HomeAPIView.as_view(), name='home_api'),
# ]
urlpatterns = [
    path('signup/', register_user, name='signup_api'),
    path('login/', login_user, name='login_api'),
    path('logout/', LogoutAPIView.as_view(), name='logout_api'),
]