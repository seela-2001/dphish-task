from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_ips, name='scan_ips'),
]