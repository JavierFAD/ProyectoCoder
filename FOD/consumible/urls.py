from consumible import views
from django.urls import path


urlpatterns = [
    path('lista_consumible/', views.ConsumibleListView.as_view() , name="Listado-Consumible"),
    path('detalle_consumible/<int:pk>/', views.ConsumibleDetailView.as_view(), name="Detalle-Consumible"),
    path('crear_consumible/', views.CreateConsumibleView.as_view(), name="Crear-Consumible"),
    path('editar_consumible/<int:pk>/', views.ConsumibleEditView.as_view(), name="Editar-Consumible"),
    path('eliminar_consumible/<int:pk>/', views.DeleteConsumibleView.as_view(), name="Eliminar-Consumible"),
]

