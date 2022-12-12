from django.urls import path
from data_manager import views

urlpatterns = [
    path('Erabiltzailea/', views.ErabiltzaileZerrenda.as_view()),
]

