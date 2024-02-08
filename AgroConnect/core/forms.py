from django import forms
from django.forms import ModelForm
from .models import CustomUser, Nave, Granjero, Veterinario


class FormularioRegistroAdministradorForm(ModelForm):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'nombre', 'apellidos']


class FormularioRegistroGranjero(ModelForm):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())

    class Meta:
        model = Granjero
        fields = ['email', 'nombre', 'apellidos']


class FormularioRegistroVeterinario(ModelForm):
    pass 


class FormularioRegistroNave(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.filter(is_inactive=False)

    class Meta:
        model = Nave
        fields = '__all__'