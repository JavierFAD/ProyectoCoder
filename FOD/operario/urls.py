from operario import views
from django.urls import path
from operario import forms


urlpatterns = [
    path('lista_operario/', views.OperarioListView.as_view() , name="Lista-Operario"),
    path('detalle_operario/<int:pk>/', views.OperarioDetailView.as_view(), name="Detalle-Operario"),
    path('crear_operario/', views.CreateOperarioView.as_view(), name="Crear-Operario"),
    path('editar_operario/<int:pk>/', views.OperarioEditView.as_view(), name="Editar-Operario"),
    path('eliminar_operario/<int:pk>/', views.DeleteOperarioView.as_view(), name="Eliminar-Operario"),
    path('buscar_operario/', views.buscar, name="Buscar-Operario"),

]

