from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import uuid
#TODO pendiente integración de imagenes
# def image_upload_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{ext}'
#     return f'media/user_profile/{filename}'

# def animal_image_upload_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{ext}'
#     return f'media/animales/{filename}'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def crear_granjero(self, email, password=None, es_granjero=True, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, es_granjero=es_granjero, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def crear_veterinario(self, email, password=None, es_veterinario=True, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, es_veterinario=es_veterinario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    es_granjero = models.BooleanField(default=False)
    es_veterinario = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # es_administrador = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email


class Granjero(CustomUser):
    granjas = models.ManyToManyField('Granja', blank=True)
    creado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.email} es granjero {self.es_granjero}' 


class Veterinario(CustomUser):
    granjas = models.ManyToManyField('Granja', blank=True)
    creado = models.DateTimeField(auto_now=True)
    modificado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.email} es veterinario {self.es_veterinario}'
    

class Direccion(models.Model):
    direccion = models.CharField(max_length=255)
    poblacion = models.CharField(max_length=255)
    provincia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.poblacion} {self.direccion}'
    

    class Meta:
        verbose_name_plural = 'Direcciones'

class Raza(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}'


class CapaAnimal(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}'


class TipoAnimal(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}'



class Enfermedad(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}'
    
    class Meta:
        verbose_name_plural = 'Enfermedades'
    

class Animal(models.Model):
    #TODO ... id with hash id
    nombre = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    capa = models.ForeignKey(CapaAnimal, on_delete=models.CASCADE)
    tipo = models.ForeignKey(verbose_name='Tipo de Animal', to=TipoAnimal, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateTimeField()
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    es_semental = models.BooleanField(default=False)
    veces_baja = models.PositiveIntegerField(default=0)
    esta_activo = models.BooleanField(default=True)
    esta_vivo = models.BooleanField(default=True)
    esta_baja = models.BooleanField(default=False)

    #TODO realizar propiedad para calcular la fecha exacta de nacimiento (días, semanas, meses, años)

    def __str__(self) -> str:
        return f'{self.nombre} {self.numero} {self.raza}'
    
    class Meta:
        verbose_name_plural = 'Animales'


# class ImagenAnimal(models.Model):
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to=animal_image_upload_path)
#     imagen_thumbnail = ImageSpecField(source='imagen',
#                                       processors=[ResizeToFill(100, 50)],
#                                       format='JPEG',
#                                       options={'quality': 60})
    
#     def __str__(self) -> str:
#         return f'{self.id} {self.animal}'


class Muerte(models.Model):
    id_animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    fecha_defuncion = models.DateTimeField()
    tipo_muerte = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.id_animal} {self.fecha_defuncion}'


class BajaEnfermedad(models.Model):
    causa_baja = models.CharField(max_length=255)
    id_animal= models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='bajas_enfermedad')
    id_enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE, related_name='bajas_enfermedad')

    def __str__(self) -> str:
        return f'{self.id_animal} {self.causa_baja}'
    
    class Meta:
        verbose_name_plural = 'Bajas por enfermedades'


class LoteCubricion(models.Model):
    nombre = models.CharField(max_length=30)
    grupo_animales = models.ManyToManyField(Animal, blank=True, related_name='grupo_animales')
    semental = models.ForeignKey(Animal, on_delete=models.CASCADE)
    fecha_cubricion = models.DateField()
    numero_cubriciones = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.nombre} {self.semental}'
    
    class Meta:
        verbose_name_plural = 'Lote de Cubriciones'


class Granja(models.Model):
    granjeros = models.ManyToManyField(Granjero, blank=True, related_name='granjeros')
    veterinarios = models.ManyToManyField(Veterinario, blank=True, related_name='veterinarios')
    animales = models.ManyToManyField(Animal, blank=True, related_name='animales')
    lotes_de_cubricion = models.ManyToManyField(LoteCubricion, blank=True, related_name='lotes_de_cubricion')
    direccion = models.OneToOneField(Direccion, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.id} {self.direccion}'
