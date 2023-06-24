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
]