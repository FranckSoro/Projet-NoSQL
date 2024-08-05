from django.urls import path
from . import views

app_name = "gestion"

urlpatterns = [
    path('', views.liste_ouvrages, name='liste_ouvrages'),
    path('creer/', views.creer_ouvrage, name='creer_ouvrage'),
    path('modifier/<int:pk>/', views.modifier_ouvrage, name='modifier_ouvrage'),
    path('supprimer/<int:pk>/', views.supprimer_ouvrage, name='supprimer_ouvrage'),
]
