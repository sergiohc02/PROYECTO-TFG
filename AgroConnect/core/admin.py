# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CustomUser, Granjero, Veterinario, Raza, CapaAnimal, TipoAnimal, Enfermedad, Animal, Muerte, BajaEnfermedad, LoteCubricion, Nave


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'email',
        'nombre',
        'apellidos',
        'es_granjero',
        'es_veterinario',
        'is_active',
        'is_staff',
        'es_administrador',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'es_granjero',
        'es_veterinario',
        'is_active',
        'is_staff',
        'es_administrador',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(Granjero)
class GranjeroAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'email',
        'nombre',
        'apellidos',
        'es_granjero',
        'es_veterinario',
        'is_active',
        'is_staff',
        'es_administrador',
        'creado',
        'modificado',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'es_granjero',
        'es_veterinario',
        'is_active',
        'is_staff',
        'es_administrador',
        'creado',
        'modificado',
    )
    raw_id_fields = ('naves',)


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'email',
        'nombre',
        'apellidos',
        'es_granjero',
        'es_veterinario',
        'is_active',
        'is_staff',
        'es_administrador',
        'creado',
        'modificado',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'es_granjero',
        'es_veterinario',
        'is_active',
        'is_staff',
        'es_administrador',
        'creado',
        'modificado',
    )
    raw_id_fields = ('naves',)


@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(CapaAnimal)
class CapaAnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(TipoAnimal)
class TipoAnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Enfermedad)
class EnfermedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'numero',
        'raza',
        'capa',
        'tipo',
        'fecha_nacimiento',
        'altura',
        'peso',
        'es_semental',
        'veces_baja',
        'esta_activo',
        'esta_vivo',
        'esta_baja',
    )
    list_filter = (
        'raza',
        'capa',
        'tipo',
        'fecha_nacimiento',
        'es_semental',
        'esta_activo',
        'esta_vivo',
        'esta_baja',
    )


@admin.register(Muerte)
class MuerteAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'fecha_defuncion', 'tipo_muerte')
    list_filter = ('animal', 'fecha_defuncion')


@admin.register(BajaEnfermedad)
class BajaEnfermedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'causa_baja', 'animal', 'enfermedad')
    list_filter = ('animal', 'enfermedad')


@admin.register(LoteCubricion)
class LoteCubricionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'semental',
        'fecha_cubricion',
        'numero_cubriciones',
    )
    list_filter = ('semental', 'fecha_cubricion')
    raw_id_fields = ('grupo_animales',)


@admin.register(Nave)
class NaveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_nave',
        'direccion',
        'poblacion',
        'provincia',
        'codigo_postal',
        'pais',
    )
    raw_id_fields = (
        'granjeros',
        'veterinarios',
        'animales',
        'lotes_de_cubricion',
    )