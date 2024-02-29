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
    FormularioRegistroAnimal, FormularioRegistroCapa, FormularioRegistroRaza, FormularioRegistroTipo
)
from .models import (
    CustomUser, Nave, Veterinario, Animal, Nacimiento, Muerte, LoteCubricion, CapaAnimal, Raza, TipoAnimal
)


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


class RegistroCapaView(LoginRequiredMixin, CreateView):
    form_class = FormularioRegistroCapa
    model = CapaAnimal
    success_url = '/dashboard/'
    template_name = 'animal/registrar-capa.html'


class RegistroRazaView(LoginRequiredMixin, CreateView):
    form_class = FormularioRegistroRaza
    model = Raza
    success_url = '/dashboard/'
    template_name = 'animal/registrar-raza.html'


class RegistroTipoView(LoginRequiredMixin, CreateView):
    form_class = FormularioRegistroTipo
    model = TipoAnimal
    success_url = '/dashboard/'
    template_name = 'animal/registrar-tipo.html'


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
        nave_seleccionada = request.POST.get('naves', None)
        return redirect('crear-lote-paso2', nave=nave_seleccionada)

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
        return render(request, 'animal/crear-lote-animales.html', context)
    elif request.method == 'POST':
        nave = Nave.objects.get(id=nave)
        animales = request.POST.getlist('animales', list())
        semental = Animal.objects.get(id=request.POST.get('semental', None))
        nombre = request.POST.get('nombre_lote', None)
        fecha_cubricion = request.POST.get('fecha_cubricion', None)

        lote = LoteCubricion.objects.create(
            nombre=nombre, nave=nave, semental=semental,
            fecha_cubricion=fecha_cubricion
        )
        lote.save()

        for i in animales:
            animal = Animal.objects.get(id=i)
            lote.grupo_animales.add(animal)
        
        lote.save()
        return redirect('dashboard-veterinario')

    else:
        return redirect('dashboard-veterinario')


class ListLotesView(LoginRequiredMixin, ListView):
    model = LoteCubricion
    template_name = 'animal/lista-lotes.html'
    context_object_name = 'lotes'

    def get_queryset(self):
        return LoteCubricion.objects.filter(nave__veterinarios=self.request.user)


class DetalleLoteView(LoginRequiredMixin, DetailView):
    model = LoteCubricion
    context_object_name = 'lote_cubricion'
    template_name = 'animal/detalle-lote-cubricion.html'


@login_required
def registro_nacimiento_paso1(request):
    if request.user.es_administrador:
        if request.method == 'POST':
            lote_seleccionado = int(request.POST.get('lote', None))
            return redirect('registro-nacimiento-paso2', lote=lote_seleccionado)

        if request.method == 'GET':
            context = {
                'lotes': LoteCubricion.objects.filter(nave__administrador=request.user)
            }
            return render(request, 'animal/registro-nacimiento-paso1.html', context)
    
    if request.user.es_veterinario:
        if request.method == 'POST':
            lote_seleccionado = int(request.POST.get('lote', None))
            return redirect('registro-nacimiento-paso2', lote=lote_seleccionado)

        if request.method == 'GET':
            context = {
                'lotes': LoteCubricion.objects.filter(nave__administrador=request.user.veterinario.administrador)
            }
            return render(request, 'animal/registro-nacimiento-paso1.html', context)

@login_required
def registro_nacimiento_paso2(request, lote):
    if request.user.es_administrador:
        if request.method == 'POST':
            lote_cubricion = LoteCubricion.objects.get(id=lote)
            nave = lote_cubricion.nave
            nombre = request.POST.get('nombre', None)
            numero = int(request.POST.get('numero', None))
            raza = Raza.objects.get(id=int(request.POST.get('raza', None)))
            capa = CapaAnimal.objects.get(id=int(request.POST.get('capa', None)))
            tipo = TipoAnimal.objects.get(id=int(request.POST.get('tipo', None)))
            fecha_nacimiento = request.POST.get('fecha_nacimiento', None)
            altura = float(request.POST.get('altura', None))
            peso = float(request.POST.get('peso', None))
            es_semental = bool(request.POST.get('es_semental', False))
            animal = Animal.objects.create(
                nave=nave, nombre=nombre, numero=numero, raza=raza, 
                capa=capa, tipo=tipo, fecha_nacimiento=fecha_nacimiento,
                altura=altura, peso=peso, es_semental=es_semental
            )
            animal.save()

            lote_cubricion.numero_cubriciones = lote_cubricion.numero_cubriciones + 1
            lote_cubricion.save()
            return redirect('registro-nacimiento-paso3', lote=lote_cubricion.id, animal=animal.id)

        if request.method == 'GET':
            context = {
                'razas': Raza.objects.all(),
                'capas': CapaAnimal.objects.all(),
                'tipos': TipoAnimal.objects.all()
            }
            return render(request, 'animal/registro-nacimiento-paso2.html', context)
    
    if request.user.es_veterinario:
        if request.method == 'POST':
            lote_cubricion = LoteCubricion.objects.get(id=lote)
            nave = lote_cubricion.nave
            nombre = request.POST.get('nombre', None)
            numero = int(request.POST.get('numero', None))
            raza = Raza.objects.get(id=int(request.POST.get('raza', None)))
            capa = CapaAnimal.objects.get(id=int(request.POST.get('capa', None)))
            tipo = TipoAnimal.objects.get(id=int(request.POST.get('tipo', None)))
            fecha_nacimiento = request.POST.get('fecha_nacimiento', None)
            altura = float(request.POST.get('altura', None))
            peso = float(request.POST.get('peso', None))
            es_semental = bool(request.POST.get('es_semental', False))
            animal = Animal.objects.create(
                nave=nave, nombre=nombre, numero=numero, raza=raza, 
                capa=capa, tipo=tipo, fecha_nacimiento=fecha_nacimiento,
                altura=altura, peso=peso, es_semental=es_semental
            )
            animal.save()

            lote_cubricion.numero_cubriciones = lote_cubricion.numero_cubriciones + 1
            lote_cubricion.save()
            return redirect('registro-nacimiento-paso3', lote=lote_cubricion.id, animal=animal.id)
        
        if request.method == 'GET':
            context = {
                'razas': Raza.objects.all(),
                'capas': CapaAnimal.objects.all(),
                'tipos': TipoAnimal.objects.all()
            }
            return render(request, 'animal/registro-nacimiento-paso2.html', context)

@login_required
def registro_nacimiento_paso3(request, lote, animal):
    if request.user.es_administrador:
        if request.method == 'POST':
            animal_hijo = Animal.objects.get(id=animal)
            lote_cubricion = LoteCubricion.objects.get(id=lote)
            madre = Animal.objects.get(id=int(request.POST.get('madre', None)))
            nacimiento = Nacimiento.objects.create(
                animal=animal_hijo, padre=lote_cubricion.semental,
                madre=madre, lote_cubricion=lote_cubricion,
                fecha_nacimiento=animal_hijo.fecha_nacimiento
            )
            nacimiento.save()
            return redirect('dashboard')

        if request.method == 'GET':
            lote_cubricion = LoteCubricion.objects.get(id=lote)
            context = {
                'madres': lote_cubricion.grupo_animales.all()
            }
            return render(request, 'animal/registro-nacimiento-paso3.html', context)
    
    if request.user.es_veterinario:
        if request.method == 'POST':
            animal_hijo = Animal.objects.get(id=animal)
            lote_cubricion = LoteCubricion.objects.get(id=lote)
            madre = Animal.objects.get(id=int(request.POST.get('madre', None)))
            nacimiento = Nacimiento.objects.create(
                animal=animal_hijo, padre=lote_cubricion.semental,
                madre=madre, lote_cubricion=lote_cubricion,
                fecha_nacimiento=animal_hijo.fecha_nacimiento
            )
            nacimiento.save()
            return redirect('dashboard-veterinario')

        if request.method == 'GET':
            lote_cubricion = LoteCubricion.objects.get(id=lote)
            context = {
                'madres': lote_cubricion.grupo_animales.all()
            }
            return render(request, 'animal/registro-nacimiento-paso3.html', context)

