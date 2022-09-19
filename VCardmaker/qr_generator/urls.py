from django.urls import path
from .views import index, qr

urlpatterns = [
    path('', index),
    path('qr', qr)
]