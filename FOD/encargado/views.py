from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Encargado
from django.urls import reverse_lazy



class EncargadoListView(LoginRequiredMixin, ListView):
    model = Encargado
    template_name = 'encargado/lista-encargado.html'

class CreateEncargadoView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Encargado
    permission_required = "encargado.add_encargado"
    template_name = 'encargado/crear-encargado.html'
    success_url = reverse_lazy('Listado-Encargado')
    fields = '__all__'


class EncargadoEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Encargado
    permission_required = "encargado.change_encargado"
    template_name = 'encargado/editar-encargado.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('Detalle-Encargado', kwargs={'pk':self.object.pk})


class DeleteEncargadoView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Encargado
    permission_required = "leader.delete_leader"
    template_name = 'encargado/eliminar-encargado.html'
    success_url = reverse_lazy('Listado-Encargado')

class EncargadoDetailView(LoginRequiredMixin, DetailView):
    model = Encargado
    template_name = 'encargado/detalle-encargado.html'


