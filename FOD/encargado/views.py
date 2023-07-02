from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Encargado
from .forms import BuscaEncargado
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
    permission_required = "encargado.delete_encargado"
    template_name = 'encargado/eliminar-encargado.html'
    success_url = reverse_lazy('Listado-Encargado')

class EncargadoDetailView(LoginRequiredMixin, DetailView):
    model = Encargado
    template_name = 'encargado/detalle-encargado.html'


def buscaEncargado(request):
    if request.method=="POST":
        busca_encargado = BuscaEncargado(request.POST)
        
        if busca_encargado.is_valid():
            data= busca_encargado.cleaned_data
            encargados = Encargado.objects.filter(apellido__icontains=data["apellido"], legajo__icontains=data["legajo"])
            return render(request, "encargado/resultado-busqueda.html", {"encargados":encargados})
        else:
            return render(request, "encargado/detalle-encargado.html")
    else:
        busca_encargado = BuscaEncargado()
        return render(request, "encargado/busca-encargado.html", {"miFormulario":busca_encargado})
    