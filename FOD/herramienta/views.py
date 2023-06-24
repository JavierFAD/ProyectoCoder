from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Herramienta
from django.urls import reverse_lazy


class HerramientaListView(LoginRequiredMixin, ListView):
    model = Herramienta
    template_name = 'herramienta/lista_herramienta.html'

class CreateHerramientaView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Herramienta
    permission_required = "herramienta.add_herramienta"
    template_name = 'herramienta/crear_herramienta.html'
    success_url = reverse_lazy('Listado-Herramienta')
    fields = '__all__'


class HerramientaEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Herramienta
    permission_required = "herramienta.change_herramienta"
    template_name = 'herramienta/editar_herramienta.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('Detalle-Herramienta', kwargs={'pk':self.object.pk})


class DeleteHerramientaView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Herramienta
    permission_required = "herramienta.delete_herramienta"
    template_name = 'herramienta/eliminar_herramienta.html'
    success_url = reverse_lazy('Listado-Herramienta')

class HerramientaDetailView(LoginRequiredMixin, DetailView):
    model = Herramienta
    template_name = 'herramienta/detalle_herramienta.html'
    
