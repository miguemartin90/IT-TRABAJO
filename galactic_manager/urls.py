"""
URL configuration for galactic_manager project.
"""

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from colonias.views import inicio_galactico  # Asegúrate de que inicio_galactico esté en colonias/views.py

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Ruta de inicio con la API de la NASA
    path("", inicio_galactico, name="inicio"),
    
    # Rutas del CRUD (módulos de tus compañeros)
    path("colonias/", include("colonias.urls")),
    
    # Sistema de Autenticación de Usuarios
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]