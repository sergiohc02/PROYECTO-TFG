from django.core.management.base import BaseCommand
from core.models import (
    Animal, BajaEnfermedad, CapaAnimal, CustomUser, 
    Direccion, Enfermedad, Granja, Granjero, LoteCubricion, 
    Muerte, Raza, TipoAnimal, Veterinario
)

class Command(BaseCommand):
    help = "Este comando sirve para crear toda la información falsa de la base de datos"

    def add_arguments(self, parser):
        parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        user1 = CustomUser.objects.create_user(email='user1@admin.com', password='1234').save()
        user2 = CustomUser.objects.create_user(email='user2@admin.com', password='1234').save()

        granjero1 = Granjero.objects.crear_granjero(email='granjero1@admin.com', password='1234').save()
        granjero2 = Granjero.objects.crear_granjero(email='granjero2@admin.com', password='1234').save()
        granjero3 = Granjero.objects.crear_granjero(email='granjero3@admin.com', password='1234').save()
        granjero4 = Granjero.objects.crear_granjero(email='granjero4@admin.com', password='1234').save()

        veterinario1 = Veterinario.objects.crear_veterinario(email='veterinario1@admin.com', password='1234').save()
        veterinario2 = Veterinario.objects.crear_veterinario(email='veterinario2@admin.com', password='1234').save()
        veterinario3 = Veterinario.objects.crear_veterinario(email='veterinario3@admin.com', password='1234').save()
        veterinario4 = Veterinario.objects.crear_veterinario(email='veterinario4@admin.com', password='1234').save()

        tipo1 = TipoAnimal.objects.create(nombre='Caballo').save()

        capa1 = CapaAnimal.objects.create(nombre='Castaño').save()

        raza1 = Raza.objects.create(nombre='Pura Raza').save()

        animal1 = Animal.objects.create(nombre='Animal1',numero='1', raza='Pura Raza', capa='Castaño', tipo='Caballo', fecha_nacimiento= ,altura= ,peso=213, es_semental= ,veces_baja= ,esta_vivo= ,esta_baja= )