from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health),
    path('registrar/', views.registrar_admision),
]
