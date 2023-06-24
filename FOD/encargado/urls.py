from encargado import views
from django.urls import path


urlpatterns = [
    path('lista_encargado/', views.EncargadoListView.as_view() , name="Listado-Encargado"),
    path('detalle_encargado/<int:pk>/', views.EncargadoDetailView.as_view(), name="Detalle-Encargado"),
    path('crear_encargado/', views.CreateEncargadoView.as_view(), name="Crear-Encargado"),
    path('editar_encargado/<int:pk>/', views.EncargadoEditView.as_view(), name="Editar-Encargado"),
    path('eliminar_encargado/<int:pk>/', views.DeleteEncargadoView.as_view(), name="Eliminar-Encargado"),
]

