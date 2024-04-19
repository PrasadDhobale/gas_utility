from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.login, name='Login'),
    path('register/', views.register, name='Register'),
    # Add more URL patterns as needed
]
