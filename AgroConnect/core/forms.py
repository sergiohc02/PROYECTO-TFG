from django import forms
from django.forms import ModelForm
from .models import CustomUser, Nave, Veterinario, Animal, Raza, CapaAnimal, TipoAnimal


class FormularioRegistroAdministradorForm(ModelForm):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'nombre', 'apellidos']


class FormularioRegistroVeterinario(ModelForm):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())

    class Meta:
        model = Veterinario
        fields = ['email', 'nombre', 'apellidos']


class FormularioRegistroNave(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['veterinarios'].queryset = Veterinario.objects.filter(administrador=self.request.user)

    class Meta:
        model = Nave
        fields = ['nombre_nave', 'veterinarios', 'direccion', 'poblacion', 'provincia', 'codigo_postal', 'pais']


class FormularioRegistroAnimal(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['nave'].queryset = Nave.objects.filter(administrador=self.request.user)

        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Animal
        fields = '__all__'


class FormularioRegistroCapa(ModelForm):   
    class Meta:
        model = CapaAnimal
        fields = '__all__'


class FormularioRegistroRaza(ModelForm):    
    class Meta:
        model = Raza
        fields = '__all__'


class FormularioRegistroTipo(ModelForm): 
    class Meta:
        model = TipoAnimal
        fields = '__all__'