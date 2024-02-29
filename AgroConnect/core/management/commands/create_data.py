from django.core.files import File
from django.core.management.base import BaseCommand
from core.models import (
    Animal, BajaEnfermedad, CapaAnimal, CustomUser, 
    Enfermedad, Nave, LoteCubricion, 
    Muerte, Nacimiento, Raza, TipoAnimal, Veterinario,
    PictureAnimal
)
from datetime import datetime, date

class Command(BaseCommand):
    help = "Este comando sirve para crear toda la información falsa de la base de datos"

    def add_arguments(self, parser):
        pass
        # parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        admin = CustomUser.objects.create_superuser(
            email='admin@admin.com', password='1234', nombre='Javier', apellidos='Fernández'
        )
        admin.save()

        user1 = CustomUser.objects.create_user(
            email='user1@admin.com', password='1234', es_administrador=True, nombre='Mario', apellidos='Fernández'
        )
        user2 = CustomUser.objects.create_user(
            email='user2@admin.com', password='1234', es_administrador=True, nombre='Raúl', apellidos='Correcueros'
        )
        user1.save()
        user2.save()

        # granjero1 = Granjero.objects.crear_granjero(administrador=admin, email='granjero1@admin.com', password='1234')
        # granjero2 = Granjero.objects.crear_granjero(administrador=admin, email='granjero2@admin.com', password='1234')
        # granjero3 = Granjero.objects.crear_granjero(administrador=admin, email='granjero3@admin.com', password='1234')
        # granjero4 = Granjero.objects.crear_granjero(administrador=admin, email='granjero4@admin.com', password='1234')
        # granjero1.save()
        # granjero2.save()
        # granjero3.save()
        # granjero4.save()

        veterinario1 = Veterinario.objects.crear_veterinario(
            administrador=user1, email='veterinario1@admin.com', password='1234', nombre='Javier',
            apellidos='Sonsola'
        )
        veterinario2 = Veterinario.objects.crear_veterinario(
            administrador=user1, email='veterinario2@admin.com', password='1234', nombre='Rodrigo',
            apellidos='Sol'
        )
        veterinario3 = Veterinario.objects.crear_veterinario(
            administrador=user2, email='veterinario3@admin.com', password='1234', nombre='Sergio',
            apellidos='Hueso'
        )
        veterinario4 = Veterinario.objects.crear_veterinario(
            administrador=user2, email='veterinario4@admin.com', password='1234', nombre='Leandro',
            apellidos='López'
        )
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

        paises = ['España']
        poblaciones = ['Calanda', 'Alcañiz', 'Zaragoza', 'Foz']
        provincias = ['Teruel']
        codigos_postales = ['44570', '55667', '67890', '54321']
        direcciones = ['C/Sierra', 'C/Solo', 'C/Alli', 'C/Perdida']

        nave1 = Nave.objects.create(
            administrador=user1,
            nombre_nave='Nave 1',
            direccion=direcciones[0], poblacion=poblaciones[0], 
            provincia=provincias[0], codigo_postal=codigos_postales[0],
            pais=paises[0]
        )
        nave1.veterinarios.add(veterinario1, veterinario2)

        nave2 = Nave.objects.create(
            administrador=user1,
            nombre_nave='Nave 2',
            direccion=direcciones[1], poblacion=poblaciones[1], 
            provincia=provincias[0], codigo_postal=codigos_postales[1],
            pais=paises[0]
        )
        nave2.veterinarios.add(veterinario1, veterinario2)

        nave3 = Nave.objects.create(
            administrador=user2,
            nombre_nave='Nave 3',
            direccion=direcciones[2], poblacion=poblaciones[2], 
            provincia=provincias[0], codigo_postal=codigos_postales[2],
            pais=paises[0]
        )
        nave3.veterinarios.add(veterinario3, veterinario4)

        nave4 = Nave.objects.create(
            administrador=user2,
            nombre_nave='Nave 4',
            direccion=direcciones[3], poblacion=poblaciones[3], 
            provincia=provincias[0], codigo_postal=codigos_postales[3],
            pais=paises[0]
        )
        nave4.veterinarios.add(veterinario3, veterinario4)

        nave1.save()
        nave2.save()
        nave3.save()
        nave4.save()

        animal1 = Animal.objects.create(nave=nave1, nombre='Animal1',numero='1', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal2 = Animal.objects.create(nave=nave1, nombre='Animal2',numero='2', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal3 = Animal.objects.create(nave=nave1, nombre='Animal3',numero='3', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal4 = Animal.objects.create(nave=nave1, nombre='Animal4',numero='4', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal5 = Animal.objects.create(nave=nave2, nombre='Animal5',numero='5', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal6 = Animal.objects.create(nave=nave2, nombre='Animal6',numero='6', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal7 = Animal.objects.create(nave=nave2, nombre='Animal7',numero='7', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal8 = Animal.objects.create(nave=nave2, nombre='Animal8',numero='8', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal9 = Animal.objects.create(nave=nave3, nombre='Animal9',numero='9', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal10 = Animal.objects.create(nave=nave3, nombre='Animal10',numero='10', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal11 = Animal.objects.create(nave=nave3, nombre='Animal11',numero='11', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal12 = Animal.objects.create(nave=nave3, nombre='Animal12',numero='12', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal13 = Animal.objects.create(nave=nave4, nombre='Animal13',numero='13', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=True)
        animal14 = Animal.objects.create(nave=nave4, nombre='Animal14',numero='14', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal15 = Animal.objects.create(nave=nave4, nombre='Animal15',numero='15', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
        animal16 = Animal.objects.create(nave=nave4, nombre='Animal16',numero='16', raza=raza1, capa=capa1, tipo=tipo1, fecha_nacimiento=datetime.now() ,altura=1.25 ,peso=213, es_semental=False)
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

        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-2.jpg', 'r+b') as image:
            file_image = File(image)

            imagen1 = PictureAnimal(
                animal=animal1, 
                imagen=file_image
                )
            imagen1.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-3.jpg', 'r+b') as image:
            file_image = File(image)

            imagen2 = PictureAnimal(
                animal=animal2, 
                imagen=file_image
                )
            imagen2.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-3.jpg', 'r+b') as image:
            file_image = File(image)

            imagen3 = PictureAnimal(
                animal=animal3, 
                imagen=file_image
                )
            imagen3.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-4.jpg', 'r+b') as image:
            file_image = File(image)

            imagen4 = PictureAnimal(
                animal=animal4, 
                imagen=file_image
                )
            imagen4.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-5.jpg', 'r+b') as image:
            file_image = File(image)

            imagen5 = PictureAnimal(
                animal=animal5, 
                imagen=file_image
                )
            imagen5.save()
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-6.jpg', 'r+b') as image:
            file_image = File(image)

            imagen6 = PictureAnimal(
                animal=animal6, 
                imagen=file_image
                )
            imagen6.save()

        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-7.jpg', 'r+b') as image:
            file_image = File(image)

            imagen7 = PictureAnimal(
                animal=animal7, 
                imagen=file_image
                )
            imagen7.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-8.jpg', 'r+b') as image:
            file_image = File(image)

            imagen8 = PictureAnimal(
                animal=animal8, 
                imagen=file_image
                )
            imagen8.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-9.jpg', 'r+b') as image:
            file_image = File(image)

            imagen9 = PictureAnimal(
                animal=animal9, 
                imagen=file_image
                )
            imagen9.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-10.jpg', 'r+b') as image:
            file_image = File(image)

            imagen10 = PictureAnimal(
                animal=animal10, 
                imagen=file_image
                )
            imagen10.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-11.jpg', 'r+b') as image:
            file_image = File(image)

            imagen11 = PictureAnimal(
                animal=animal11, 
                imagen=file_image
                )
            imagen11.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-12.jpg', 'r+b') as image:
            file_image = File(image)

            imagen12 = PictureAnimal(
                animal=animal12, 
                imagen=file_image
                )
            imagen12.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-13.jpg', 'r+b') as image:
            file_image = File(image)

            imagen13 = PictureAnimal(
                animal=animal13, 
                imagen=file_image
                )
            imagen13.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-14.jpg', 'r+b') as image:
            file_image = File(image)

            imagen14 = PictureAnimal(
                animal=animal14, 
                imagen=file_image
                )
            imagen14.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-2.jpg', 'r+b') as image:
            file_image = File(image)

            imagen15 = PictureAnimal(
                animal=animal15, 
                imagen=file_image
                )
            imagen15.save()
        
        with open('C:\\Users\\sergi\\OneDrive\\Desktop\\PROYECTO - TFG\\AgroConnect\\core\\static\\images\\caballos\\caballo-3.jpg', 'r+b') as image:
            file_image = File(image)

            imagen16 = PictureAnimal(
                animal=animal16, 
                imagen=file_image
                )
            imagen16.save()
        

        lote_cubricion1 = LoteCubricion.objects.create(
            nave=nave1, nombre='Lote1',semental=animal1, fecha_cubricion=date(2024, 1, 30))
        lote_cubricion1.grupo_animales.add(animal2, animal3, animal4)
        lote_cubricion2 = LoteCubricion.objects.create(
            nave=nave2, nombre='Lote2',semental=animal5, fecha_cubricion=date(2024, 1, 30)
        )
        lote_cubricion2.grupo_animales.add(animal6, animal7, animal8)
        lote_cubricion3 = LoteCubricion.objects.create(
            nave=nave3, nombre='Lote3',semental=animal9, fecha_cubricion=date(2024, 1, 30)
        )
        lote_cubricion3.grupo_animales.add(animal10, animal11, animal12)
        lote_cubricion4 = LoteCubricion.objects.create(
            nave=nave4, nombre='Lote4',semental=animal13, fecha_cubricion=date(2024, 1, 30)
        )
        lote_cubricion4.grupo_animales.add(animal14, animal15, animal16)

        lote_cubricion1.save()
        lote_cubricion2.save()
        lote_cubricion3.save()
        lote_cubricion4.save()

        # Nacimientos
        animal_nacido1 = Animal.objects.create(
            nave=nave1, nombre='Rit', numero=12, raza=raza1,
            capa=capa1, tipo=tipo1, fecha_nacimiento=date(2024, 2, 20),
            altura=1.23, peso=80
        )
        animal_nacido1.save()

        nacimiento1 = Nacimiento.objects.create(
            animal=animal_nacido1, padre=animal1, madre=animal2,
            lote_cubricion=lote_cubricion1,
            fecha_nacimiento=animal_nacido1.fecha_nacimiento
        )
        nacimiento1.save()

        animal_nacido2 = Animal.objects.create(
            nave=nave2, nombre='Seser', numero=14, raza=raza1,
            capa=capa1, tipo=tipo1, fecha_nacimiento=date(2024, 2, 20),
            altura=1.23, peso=80
        )
        animal_nacido2.save()

        nacimiento2 = Nacimiento.objects.create(
            animal=animal_nacido2, padre=animal5, madre=animal6,
            lote_cubricion=lote_cubricion2,
            fecha_nacimiento=animal_nacido2.fecha_nacimiento
        )
        nacimiento2.save()

        animal_nacido3 = Animal.objects.create(
            nave=nave3, nombre='Sr', numero=34, raza=raza1,
            capa=capa1, tipo=tipo1, fecha_nacimiento=date(2024, 2, 20),
            altura=1.23, peso=80
        )
        animal_nacido3.save()

        nacimiento3 = Nacimiento.objects.create(
            animal=animal_nacido3, padre=animal9, madre=animal10,
            lote_cubricion=lote_cubricion3,
            fecha_nacimiento=animal_nacido3.fecha_nacimiento
        )
        nacimiento3.save()

        animal_nacido4 = Animal.objects.create(
            nave=nave4, nombre='Tirachinas', numero=11, raza=raza1,
            capa=capa1, tipo=tipo1, fecha_nacimiento=date(2024, 2, 20),
            altura=1.23, peso=80
        )
        animal_nacido4.save()

        nacimiento4 = Nacimiento.objects.create(
            animal=animal_nacido4, padre=animal13, madre=animal14,
            lote_cubricion=lote_cubricion4,
            fecha_nacimiento=animal_nacido4.fecha_nacimiento
        )
        nacimiento4.save()

        #MUERTES
        muerte1 = Muerte.objects.create(
            animal=animal3, fecha_muerte=date(2024, 2, 20)
        )
        muerte1.save()

        animal3.veces_baja = 1
        animal3.esta_vivo = False
        animal3.esta_baja = True
        animal3.save()

        muerte2 = Muerte.objects.create(
            animal=animal7, fecha_muerte=date(2024, 2, 20)
        )
        muerte2.save()

        animal7.veces_baja = 1
        animal7.esta_vivo = False
        animal7.esta_baja = True
        animal7.save()

        muerte3 = Muerte.objects.create(
            animal=animal11, fecha_muerte=date(2024, 2, 20)
        )
        muerte3.save()

        animal11.veces_baja = 1
        animal11.esta_vivo = False
        animal11.esta_baja = True
        animal11.save()

        muerte4 = Muerte.objects.create(
            animal=animal15, fecha_muerte=date(2024, 2, 20)
        )
        muerte4.save()

        animal15.veces_baja = 1
        animal15.esta_vivo = False
        animal15.esta_baja = True
        animal15.save()