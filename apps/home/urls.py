# from django.urls import path, include
# from . import views
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('', views.HomeView.as_view(), name='home'),  
#     path('login', views.LoginInterfaceView.as_view(), name='login'),
#     #path('logout/', auth_views.LogoutView.as_view(template_name='logout.html', next_page='/login'), name='logout'),
#     path('logout/', views.LogoutInterfaceView.as_view(next_page='/login'), name='logout'),
#     path('register', views.SignUpView.as_view(), name='register'),
#     path('api/home/', include('apps.home.api_urls')),  # API endpoints
# ]
