from django.urls import path
from . import views

app_name = 'service_requests'

urlpatterns = [
    path('', views.submit_service_request, name='submit_request'),
    path('track/', views.track_service_request, name='track_request'),
    # Add more URL patterns as needed
]
