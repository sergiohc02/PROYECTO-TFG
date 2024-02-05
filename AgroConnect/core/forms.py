from django import forms
from django.forms import ModelForm
from .models import CustomUser


class FormularioRegistroAdministradorForm(ModelForm):
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'nombre', 'apellidos']