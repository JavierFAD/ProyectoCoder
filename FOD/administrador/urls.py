from django.urls import path
from administrador import views


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('perfil/', views.mostrar_perfil, name='mostrar-cuenta'),
    path('perfil/eliminar/<int:pk>/', views.EliminarPerfil.as_view(), name='eliminar-cuenta'),
    path('perfil/editar/', views.editar_perfil, name='editar-cuenta'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('perfil/cambiar-password/', views.CambiarPassword.as_view(), name='cambiar-pass'),
    path('solicitud/', views.CreatemensajeView.as_view(), name='solicitud'),
    path('succes/', views.succes, name='solicitud-exitosa'),
    path('mensajes/', views.VerMensajesViews.as_view(), name='listado-mensajes'),
    path('mensajes/mensaje/<int:pk>/', views.DetalleMensajeView.as_view(), name='ver-mensaje'),
    path('mensajes/mensaje/eliminar/<int:pk>', views.BorrarMensajeView.as_view(), name='eliminar-mensaje'),
]