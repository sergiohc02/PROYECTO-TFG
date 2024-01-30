from django.core.management.base import BaseCommand
from core.models import (
    Animal, BajaEnfermedad, CapaAnimal, CustomUser, 
    Direccion, Enfermedad, Granja, Granjero, LoteCubricion, 
    Muerte, Raza, TipoAnimal, Veterinario
)
from datetime import datetime, date

class Command(BaseCommand):
    help = "Este comando sirve para crear toda la información falsa de la base de datos"

    def add_arguments(self, parser):
        pass
        # parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        admin = CustomUser.objects.create_superuser(email='admin@admin.com', password='1234')
        admin.save()

        user1 = CustomUser.objects.create_user(email='user1@admin.com', password='1234')
        user2 = CustomUser.objects.create_user(email='user2@admin.com', password='1234')
        user1.save()
        user2.save()

        granjero1 = Granjero.objects.crear_granjero(email='granjero1@admin.com', password='1234')
        granjero2 = Granjero.objects.crear_granjero(email='granjero2@admin.com', password='1234')
        granjero3 = Granjero.objects.crear_granjero(email='granjero3@admin.com', password='1234')
        granjero4 = Granjero.objects.crear_granjero(email='granjero4@admin.com', password='1234')
        granjero1.save()
        granjero2.save()
        granjero3.save()
        granjero4.save()

        veterinario1 = Veterinario.objects.crear_veterinario(email='veterinario1@admin.com', password='1234')
        veterinario2 = Veterinario.objects.crear_veterinario(email='veterinario2@admin.com', password='1234')
        veterinario3 = Veterinario.objects.crear_veterinario(email='veterinario3@admin.com', password='1234')
        veterinario4 = Veterinario.objects.crear_veterinario(email='veterinario4@admin.com', password='1234')
        veterinario1.save()
        veterinario2.save()
        veterinario3.save()
        veterinario4.save()

        tipo1 = TipoAnimal.objects.create(nombre='Caballo')
        tipo1.save()

        capa1 = CapaAnimal.objects.create(nombre='Castaño')
        capa1.save()

        raza1 = Raza.objects.create(nombre='Pura Raza')
        raza1.save()

        animal1 = Animal.objects.create(nombre='Animal1',numero='1', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal2 = Animal.objects.create(nombre='Animal2',numero='2', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal3 = Animal.objects.create(nombre='Animal3',numero='3', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal4 = Animal.objects.create(nombre='Animal4',numero='4', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal5 = Animal.objects.create(nombre='Animal5',numero='5', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal6 = Animal.objects.create(nombre='Animal6',numero='6', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal7 = Animal.objects.create(nombre='Animal7',numero='7', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal8 = Animal.objects.create(nombre='Animal8',numero='8', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal9 = Animal.objects.create(nombre='Animal9',numero='9', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal10 = Animal.objects.create(nombre='Animal10',numero='10', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal11 = Animal.objects.create(nombre='Animal11',numero='11', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal12 = Animal.objects.create(nombre='Animal12',numero='12', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal13 = Animal.objects.create(nombre='Animal13',numero='13', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal14 = Animal.objects.create(nombre='Animal14',numero='14', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal15 = Animal.objects.create(nombre='Animal15',numero='15', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal16 = Animal.objects.create(nombre='Animal16',numero='16', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal1.save()
        animal2.save()
        animal3.save()
        animal4.save()
        animal5.save()
        animal6.save()
        animal7.save()
        animal8.save()
        animal9.save()
        animal10.save()
        animal11.save()
        animal12.save()
        animal13.save()
        animal14.save()
        animal15.save()
        animal16.save()

        paises = ['España']
        poblaciones = ['Calanda', 'Alcañiz', 'Zaragoza', 'Foz']
        provincias = ['Teruel']
        codigos_postales = ['44570', '55667', '67890', '54321']
        direcciones = ['C/Sierra', 'C/Solo', 'C/Alli', 'C/Perdida']

        direccion1 = Direccion.objects.create(direccion=direcciones[0], poblacion=poblaciones[0], 
                                              provincia=provincias[0], codigo_postal=codigos_postales[0],
                                              pais=paises[0]
                                              )
        direccion2 = Direccion.objects.create(direccion=direcciones[1], poblacion=poblaciones[1], 
                                              provincia=provincias[0], codigo_postal=codigos_postales[1],
                                              pais=paises[0]
                                              )
        direccion3 = Direccion.objects.create(direccion=direcciones[2], poblacion=poblaciones[2], 
                                              provincia=provincias[0], codigo_postal=codigos_postales[2],
                                              pais=paises[0]
                                            )
        direccion4 = Direccion.objects.create(direccion=direcciones[3], poblacion=poblaciones[3], 
                                              provincia=provincias[0], codigo_postal=codigos_postales[3],
                                              pais=paises[0]
                                            )
        direccion1.save()
        direccion2.save()
        direccion3.save()
        direccion4.save()

        lote_cubricion1 = LoteCubricion.objects.create(nombre='Lote1',semental=animal1, fecha_cubricion=date(2024, 1, 30))
        lote_cubricion1.grupo_animales.add(animal1, animal2, animal3, animal4)
        lote_cubricion2 = LoteCubricion.objects.create(
            nombre='Lote2',semental=animal5, fecha_cubricion=date(2024, 1, 30)
        )
        lote_cubricion2.grupo_animales.add(animal5, animal6, animal7, animal8)
        lote_cubricion3 = LoteCubricion.objects.create(
            nombre='Lote3',semental=animal9, fecha_cubricion=date(2024, 1, 30)
        )
        lote_cubricion3.grupo_animales.add(animal9, animal10, animal11, animal12)
        lote_cubricion4 = LoteCubricion.objects.create(
            nombre='Lote4',semental=animal13, fecha_cubricion=date(2024, 1, 30)
        )
        lote_cubricion4.grupo_animales.add(animal13, animal14, animal15, animal16)

        lote_cubricion1.save()
        lote_cubricion2.save()
        lote_cubricion3.save()
        lote_cubricion4.save()

        granja1 = Granja.objects.create(
            direccion=direccion1
        )
        granja1.animales.add(animal1, animal2, animal3, animal4)
        granja1.granjeros.add(granjero1)
        granja1.veterinarios.add(veterinario1)
        granja1.lotes_de_cubricion.add(lote_cubricion1)

        granja2 = Granja.objects.create(
            direccion=direccion2
        )
        granja2.animales.add(animal5, animal6, animal7, animal8)
        granja2.granjeros.add(granjero2)
        granja2.veterinarios.add(veterinario2)
        granja2.lotes_de_cubricion.add(lote_cubricion2)

        granja3 = Granja.objects.create(
            direccion=direccion3
        )
        granja3.animales.add(animal9, animal10, animal11, animal12)
        granja3.granjeros.add(granjero3)
        granja3.veterinarios.add(veterinario3)
        granja3.lotes_de_cubricion.add(lote_cubricion3)

        granja4 = Granja.objects.create(
            direccion=direccion4
        )
        granja4.animales.add(animal13, animal14, animal15, animal16)
        granja4.granjeros.add(granjero4)
        granja4.veterinarios.add(veterinario4)
        granja4.lotes_de_cubricion.add(lote_cubricion4)

        granja1.save()
        granja2.save()
        granja3.save()
        granja4.save()
