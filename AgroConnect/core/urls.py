"""
URL configuration for AgroConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.PaginaAcceso.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registro/', views.RegistroAdministrador.as_view(), name='registro-administrador'),
    path('password_reset/', views.PasswordReset.as_view(), name='password-reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset_done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset_complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard_veterinario/', views.DashboardVeterinarioView.as_view(), name='dashboard-veterinario'),
    path('dashboard/naves/', views.ListNavesView.as_view(), name='lista-naves'),
    path('dashboard/registro_nave/', views.RegistroNaveView.as_view(), name='registro-nave'),
    path('dashboard/detalle_nave/<int:pk>/', views.DetalleNaveView.as_view(), name='detalle-nave'),
    path('dashboard/veterinarios/', views.ListVeterinariosView.as_view(), name='lista-veterinarios'),
    path('dashboard/registro_veterinario/', views.RegistroVeterinarioView.as_view(), name='registro-veterinario'),
    path('dashboard/animales/', views.ListAnimalesView.as_view(), name='lista-animales'),
    path('dashboard/registrar_animal/', views.RegistroAnimalView.as_view(), name='registro-animal'),
    path('dashboard/animal_detalle/<int:pk>/', views.AnimalDetalleView.as_view(), name='detalle-animal'),
]
