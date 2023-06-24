from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Consumible
from django.urls import reverse_lazy


class ConsumibleListView(LoginRequiredMixin, ListView):
    model = Consumible
    template_name = 'consumible/lista_consumible.html'

class CreateConsumibleView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Consumible
    permission_required = "consumible.add_consumible"
    template_name = 'consumible/crear_consumible.html'
    success_url = reverse_lazy('Listado-Consumible')
    fields = '__all__'


class ConsumibleEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Consumible
    permission_required = "consumible.change_consumible"
    template_name = 'consumible/editar_consumible.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('Detalle-Consumible', kwargs={'pk':self.object.pk})


class DeleteConsumibleView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Consumible
    permission_required = "consumible.delete_consumible"
    template_name = 'consumible/eliminar_consumible.html'
    success_url = reverse_lazy('Listado-Consumible')

class ConsumibleDetailView(LoginRequiredMixin, DetailView):
    model = Consumible
    template_name = 'consumible/detalle_consumible.html'