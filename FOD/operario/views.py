from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Operario
from .forms import BuscaOperario, BuscaLegajo
from django.urls import reverse_lazy

class OperarioListView(LoginRequiredMixin, ListView):
    model = Operario
    template_name = 'operario/lista-operario.html'

class CreateOperarioView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Operario
    permission_required = "operario.add_operario"
    template_name = 'operario/crear-operario.html'
    success_url = reverse_lazy('Lista-Operario')
    fields = '__all__'


class OperarioEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Operario
    permission_required = "operario.change_operario"
    template_name = 'operario/editar-operario.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('Detalle-Operario', kwargs={'pk':self.object.pk})


class DeleteOperarioView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Operario
    permission_required = "operario.delete_operario"
    template_name = 'operario/eliminar-operario.html'
    success_url = reverse_lazy('Lista-Operario')

class OperarioDetailView(LoginRequiredMixin, DetailView):
    model = Operario
    template_name = 'operario/detalle-operario.html'
    

def buscar(request):
    if request.method=="POST":
        busca_operario = BuscaOperario(request.POST)
        
        if busca_operario.is_valid():
            info = busca_operario.cleaned_data
            operarios = Operario.objects.filter(apellido__icontains=info["apellido"])
            return render(request, "operario/resultado-busqueda.html", {"operarios": operarios})
        else:
            return render(request, "operario/detalle-operario.html")
    else:
        busca_operario = BuscaOperario()
        return render(request, "operario/busca-operario.html", {"miFormulario": busca_operario})
    
def buscarLegajo(request):
    if request.method=="POST":
        busca_operario = BuscaLegajo(request.POST)
        
        if busca_operario.is_valid():
            info = busca_operario.cleaned_data
            operarios = Operario.objects.filter(legajo__icontains=info["legajo"])
            return render(request, "operario/resultado-busqueda.html", {"operarios": operarios})
        else:
            return render(request, "operario/detalle-operario.html")
    else:
        busca_operario = BuscaLegajo()
        return render(request, "operario/busca-legajo.html", {"miFormulario": busca_operario})