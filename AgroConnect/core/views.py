from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView,
    PasswordResetCompleteView
)

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    FormularioRegistroAdministradorForm, FormularioRegistroNave, FormularioRegistroGranjero, FormularioRegistroVeterinario
)
from .models import CustomUser, Nave, Granjero


class PaginaAcceso(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid email or password')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'AgroConnect'
        return context


class LogoutView(LogoutView):
    next_page = '/login/'


class PasswordReset(PasswordResetView):
    success_url = reverse_lazy('password_reset_done')


class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy('password_reset_complete')


class PasswordResetDone(PasswordResetDoneView):
    extra_context = {
        'titulo': 'AgroConnect'
    }


class PasswordResetComplete(PasswordResetCompleteView):
    extra_context = {
        'titulo': 'AgroConnect'
    }


class RegistroAdministrador(CreateView):
    form_class = FormularioRegistroAdministradorForm
    model = CustomUser
    success_url = '/login/'
    template_name = 'registration/registro-administrador.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        password = form.cleaned_data['password']
        self.object.set_password(password)
        self.object.es_administrador = True
        self.object.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'AgroConnect'
        return context
    

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'AgroConnect'
        return context


class RegistroGranjero(LoginRequiredMixin, CreateView):
    form_class = FormularioRegistroGranjero
    model = Granjero
    success_url = '/dashboard/'
    template_name = 'granjero/registrar-granjero.html'

    def form_valid(self, form):
        self.object = form.save()
        form.instance.administrador = self.request.user
        password = form.cleaned_data['password']
        self.object.set_password(password)
        self.object.es_granjero = True
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'AgroConnect'
        return context



class RegistroNaveView(LoginRequiredMixin, CreateView):
    form_class = FormularioRegistroNave
    model = Nave
    success_url = '/dashboard/'
    template_name = 'nave/registrar-nave.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'AgroConnect'
        return context