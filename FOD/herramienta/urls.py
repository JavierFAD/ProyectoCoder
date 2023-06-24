from django.urls import path
from herramienta import views


urlpatterns = [
    path('lista_herramienta/', views.HerramientaListView.as_view() , name="Listado-Herramienta"),
    path('detalle_herramienta/<int:pk>/', views.HerramientaDetailView.as_view(), name="Detalle-Herramienta"),
    path('crear_herramienta/', views.CreateHerramientaView.as_view(), name="Crear-Herramienta"),
    path('editar_herramienta/<int:pk>/', views.HerramientaEditView.as_view(), name="Editar-Herramienta"),
    path('eliminar_herramienta/<int:pk>/', views.DeleteHerramientaView.as_view(), name="Eliminar-Herramienta"),
]

