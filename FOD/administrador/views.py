from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.views.generic import DeleteView, CreateView, DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from administrador import forms
from administrador import models


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect("Home")
            else:
                return render(request, "administrador/iniciar-sesion.html", {"mensaje":"Los datos ingresados son incorrectos"})

    form = AuthenticationForm()
    return render(request, "administrador/iniciar-sesion.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "administrador/crear-cuenta.html", {"form":form})

    form = forms.RegistroUsuarioForm()
    return render(request, "administrador/crear-cuenta.html", {"form":form})

@login_required
def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _ = models.Administrador.objects.get_or_create(user=usuario)
    if request.method == "POST":
        form = forms.EditarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                usuario.first_name = data.get('first_name')
            if data.get('last_name'):
                usuario.last_name = data.get('last_name')
            usuario.email = data.get('email') if data.get('email') else usuario.email
            modelo_perfil.avatar = data.get('avatar') if data.get('avatar') else modelo_perfil.avatar

            modelo_perfil.save()
            usuario.save()
            return redirect("mostrar-cuenta")
        else:
            return render(request, 'administrador/editar-cuenta.html', {'form': form})

    form = forms.EditarUsuarioForm(
        initial={
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'email': usuario.email,
            'avatar': modelo_perfil.avatar
        }
    )
    return render(request, 'administrador/editar-cuenta.html', {'form': form})


@login_required 
def mostrar_perfil(request):
    return render(request, 'administrador/mostrar-cuenta.html')

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'administrador/cambiar-pass.html'
    success_url = reverse_lazy("mostrar-cuenta")
    

class EliminarPerfil(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("Home")
    template_name = 'administrador/eliminar-cuenta.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'administrador/cerrar-sesion.html'

def succes(request):
    return render(request, "administrador/solicitud_exitosa.html")

#Mensajes
class CreatemensajeView(LoginRequiredMixin, CreateView):
    model = models.Mensaje
    template_name = 'administrador/solicitud_staff.html'
    success_url = reverse_lazy('solicitud-exitosa')
    fields = '__all__'
    

class VerMensajesViews(LoginRequiredMixin, ListView):
    model = models.Mensaje
    template_name = 'administrador/lista-mensajes.html'
    
class DetalleMensajeView(LoginRequiredMixin, DetailView):
    model = models.Mensaje
    template_name = 'administrador/ver-mensaje.html'
    
class BorrarMensajeView(LoginRequiredMixin, DeleteView):
    model = models.Mensaje
    success_url = reverse_lazy('listado-mensajes')
    template_name = "administrador/eliminar-mensaje.html"