from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView,
    PasswordResetCompleteView
)

from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import (
    FormularioRegistroAdministradorForm, FormularioRegistroNave, FormularioRegistroVeterinario,
    FormularioRegistroAnimal
)
from .models import CustomUser, Nave, Veterinario, Animal, Nacimiento, Muerte


class PaginaAcceso(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('admin:index')
        elif self.request.user.es_veterinario:
            return reverse_lazy('dashboard-veterinario')
        
        return reverse_lazy('dashboard')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid email or password')
        return self.render_to_response(self.get_context_data(form=form))


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
        context['naves'] = Nave.objects.filter(administrador=self.request.user)
        context['animales'] = Animal.objects.filter(nave__administrador=self.request.user)
        context['numero_naves'] = Nave.objects.filter(administrador=self.request.user).count()
        context['nacimientos'] = Nacimiento.objects.filter(animal__nave__administrador=self.request.user).count()
        context['muertes'] = Muerte.objects.filter(animal__nave__administrador=self.request.user).count()
        context['veterinarios'] = Veterinario.objects.filter(administrador=self.request.user).count()
        context['numero_animales'] = Animal.objects.filter(nave__administrador=self.request.user).count()
        context['animales_vivos'] = Animal.objects.filter(nave__administrador=self.request.user, esta_vivo=True).count()
        context['animales_baja'] = Animal.objects.filter(nave__administrador=self.request.user, esta_baja=True).count()
        context['animales_muertos'] = Animal.objects.filter(nave__administrador=self.request.user, esta_vivo=False).count()
        return context


class DashboardVeterinarioView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard-veterinario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['granjero'] = self.request.user.veterinario.administrador.nombre
        context['naves'] = Nave.objects.filter(administrador=self.request.user)
        context['animales'] = Animal.objects.filter(nave__administrador=self.request.user.veterinario.administrador)
        context['numero_naves'] = Nave.objects.filter(administrador=self.request.user.veterinario.administrador).count()
        context['numero_animales'] = Animal.objects.filter(nave__administrador=self.request.user.veterinario.administrador).count()
        context['animales_vivos'] = Animal.objects.filter(nave__administrador=self.request.user.veterinario.administrador, esta_vivo=True).count()
        context['animales_baja'] = Animal.objects.filter(nave__administrador=self.request.user.veterinario.administrador, esta_baja=True).count()
        context['animales_muertos'] = Animal.objects.filter(nave__administrador=self.request.user.veterinario.administrador, esta_vivo=False).count()
        return context

class RegistroVeterinarioView(LoginRequiredMixin, CreateView):
    form_class = FormularioRegistroVeterinario
    model = Veterinario
    success_url = '/dashboard/'
    template_name = 'veterinario/registrar-veterinario.html'

    def form_valid(self, form):
        form.instance.administrador = self.request.user
        password = form.cleaned_data['password']
        form.instance.set_password(password)
        form.instance.es_veterinario = True
        self.object = form.save()
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
    
    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        if hasattr(self, "object"):
            kwargs.update({"instance": self.object})
        return kwargs
    
    def form_valid(self, form):
        form.instance.administrador = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class RegistroAnimalView(LoginRequiredMixin, CreateView):
    form_class = FormularioRegistroAnimal
    model = Animal
    success_url = '/dashboard/'
    template_name = 'animal/registrar-animal.html'

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        if hasattr(self, "object"):
            kwargs.update({"instance": self.object})
        return kwargs


class DetalleNaveView(LoginRequiredMixin, DetailView):
    model = Nave
    context_object_name = 'nave'
    template_name = 'nave/detalle-nave.html'

    # def get_queryset(self):
    #     return Nave.objects.get(id=self.kwargs['pk'])


class AnimalDetalleView(LoginRequiredMixin, DetailView):
    model = Animal
    context_object_name = 'animal'
    template_name = 'animal/detalle-animal.html'


class ListNavesView(LoginRequiredMixin, ListView):
    model = Nave
    template_name = 'nave/lista-naves.html'
    context_object_name = 'naves'

    def get_queryset(self):
        if self.request.user.es_veterinario:
            administrador = self.request.user.veterinario.administrador
            return Nave.objects.filter(administrador=administrador)
        
        return Nave.objects.filter(administrador=self.request.user)


class ListAnimalesView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animal/lista-animales.html'
    context_object_name = 'animales'

    def get_queryset(self):
        if self.request.user.es_veterinario:
            administrador = self.request.user.veterinario.administrador
            return Animal.objects.filter(nave__administrador=administrador)
        
        return Animal.objects.filter(nave__administrador=self.request.user)


class ListVeterinariosView(LoginRequiredMixin, ListView):
    model = Veterinario
    template_name = 'veterinario/lista-veterinarios.html'
    context_object_name = 'veterinarios'

    def get_queryset(self):
        return Veterinario.objects.filter(administrador=self.request.user)

@login_required
def crear_lote_seleccion_nave(request):
    if request.method == 'GET':
        context = {
            'naves': Nave.objects.filter(administrador=request.user.veterinario.administrador)
        }
        return render(request, 'animal/crear-lote-naves.html', context)
    elif request.method == 'POST':
        nave_seleccionada = request.POST['naves']

    else:
        return redirect('dashboard-veterinario')

@login_required
def crear_lote_seleccion_animales(request, nave):
    if request.method == 'GET':
        context = {
            'animales': Animal.objects.filter(
                nave__administrador=request.user.veterinario.administrador,
                nave=nave,
                es_semental=False
            ),

            'sementales': Animal.objects.filter(
               nave__administrador=request.user.veterinario.administrador,
               nave=nave,
               es_semental=True
            )
        }
        return render(request, 'animal/crear-lote-naves.html', context)
    elif request.method == 'POST':
        nave_seleccionada = request.POST['naves']
        
    else:
        return redirect('dashboard-veterinario')