# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CustomUser, Granjero, Veterinario, Direccion, Raza, CapaAnimal, TipoAnimal, Enfermedad, Animal, Muerte, BajaEnfermedad, LoteCubricion, Granja


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
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'es_granjero',
        'es_veterinario',
        'is_active',
        'is_staff',
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
        'creado',
        'modificado',
    )
    raw_id_fields = ('granjas',)


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
        'creado',
        'modificado',
    )
    raw_id_fields = ('granjas',)


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'direccion',
        'poblacion',
        'provincia',
        'codigo_postal',
        'pais',
    )


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
    list_display = ('id', 'id_animal', 'fecha_defuncion', 'tipo_muerte')
    list_filter = ('id_animal', 'fecha_defuncion')


@admin.register(BajaEnfermedad)
class BajaEnfermedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'causa_baja', 'id_animal', 'id_enfermedad')
    list_filter = ('id_animal', 'id_enfermedad')


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


@admin.register(Granja)
class GranjaAdmin(admin.ModelAdmin):
    list_display = ('id', 'direccion')
    list_filter = ('direccion',)
    raw_id_fields = ('animales', 'lotes_de_cubricion')