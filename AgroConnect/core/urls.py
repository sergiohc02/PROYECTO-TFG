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
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard_veterinario/', views.DashboardVeterinarioView.as_view(), name='dashboard-veterinario'),
    path('dashboard/naves/', views.ListNavesView.as_view(), name='lista-naves'),
    path('dashboard/registro_nave/', views.RegistroNaveView.as_view(), name='registro-nave'),
    path('dashboard/detalle_nave/<int:pk>/', views.DetalleNaveView.as_view(), name='detalle-nave'),
    path('dashboard/editar_nave/<int:pk>/', views.EditarNaveView.as_view(), name='editar-nave'),
    path('dashboard/veterinarios/', views.ListVeterinariosView.as_view(), name='lista-veterinarios'),
    path('dashboard/registro_veterinario/', views.RegistroVeterinarioView.as_view(), name='registro-veterinario'),
    path('dashboard/animales/', views.ListAnimalesView.as_view(), name='lista-animales'),
    path('dashboard/registrar_animal/', views.RegistroAnimalView.as_view(), name='registro-animal'),
    path('dashboard/editar_animal/<int:pk>/', views.EdicionAnimalView.as_view(), name='edicion-animal'),
    path('dashboard/borrar_animal/<int:pk>/', views.BorrarAnimalView.as_view(), name='borrar-animal'),
    path('dashboard/animal_detalle/<int:pk>/', views.AnimalDetalleView.as_view(), name='detalle-animal'),
    path('dashboard/animal_detalle/<int:animal>/baja/', views.animal_baja, name='baja-animal'),
    path('dashboard/animal_detalle/<int:animal>/alta/', views.animal_alta, name='alta-animal'),
    path('dashboard/animal_detalle/<int:animal>/muerte/', views.animal_muerte, name='muerte-animal'),
    path('dashboard/animal_detalle/<int:animal>/enfermedad/', views.animal_enfermedad, name='enfermedad-animal'),
    path('dashboard/creacion_capa/', views.RegistroCapaView.as_view(), name='registro-capa'),
    path('dashboard/creacion_raza/', views.RegistroRazaView.as_view(), name='registro-raza'),
    path('dashboard/creacion_tipo/', views.RegistroTipoView.as_view(), name='registro-tipo'),
    path('dashboard/lotes/', views.ListLotesView.as_view(), name='lista-lotes'),
    path('dashboard/detalle_lote/<int:pk>/', views.DetalleLoteView.as_view(), name='detalle-lote'),
    path('dashboard/edicion_lote/<int:pk>/', views.EdicionLoteView.as_view(), name='edicion-lote'),
    path('dashboard/borrar_lote/<int:pk>/', views.BorrarLoteView.as_view(), name='borrar-lote'),
    path('dashboard/registrar_nacimiento/', views.registro_nacimiento_paso1, name='registro-nacimiento-paso1'),
    path(
        'dashboard/registrar_nacimiento/lote/<int:lote>/', 
        views.registro_nacimiento_paso2, name='registro-nacimiento-paso2'
    ),
    path(
        'dashboard/registrar_nacimiento/lote/<int:lote>/animal_nacido/<int:animal>/',
        views.registro_nacimiento_paso3, name='registro-nacimiento-paso3'
    ),
    path('lote_cubricion/crear/', views.crear_lote_seleccion_nave, name='crear-lote-paso1'),
    path('lote_cubricion/crear/<int:nave>/', views.crear_lote_seleccion_animales, name='crear-lote-paso2'),
    path('crear/enfermedad/', views.crear_enfermedad, name='crear-enfermedad'),
    path('crear/pdf/', views.crear_pdf, name='crear-pdf'),
]
