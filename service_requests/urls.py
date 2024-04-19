from django.urls import path
from . import views

app_name = 'service_requests'

urlpatterns = [
    path('submit', views.submit_service_request, name='submit_request'),
    path('track/', views.track_service_request, name='track_request'),    
]
