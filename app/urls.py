from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.index, name='index'),
    path('ciudades/<str:id_ciudad>/', views.ciudades, name='ciudades'),
    path('usuarios/<str:id_usuario>/', views.usuarios, name='usuarios'),
    path('busqueda?busqueda=/', views.busqueda, name='busqueda'),
]