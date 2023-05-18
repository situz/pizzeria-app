"""Defines URL patterns for users."""
'''
from django.conf.urls import url
#from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Login page
    path(r'^login/$', auth_views.LoginView.as_view(), {'template_name' : 'users/login.html'}, name='login'),
]
'''
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('register/', views.register, name='register'),
]
