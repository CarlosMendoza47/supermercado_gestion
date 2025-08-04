from django.urls import path
from .views import login_view, logout_view, inicio, registro_usuario

urlpatterns = [
    path('', login_view, name='login'),      # Página de inicio
    path('login/', login_view, name='login'),
    path('inicio/', inicio, name='inicio'),
    path('logout/', logout_view, name='logout'),
    path('accounts/login/', login_view, name='login_redirect'),  # Redirección para login
    # Puedes agregar más rutas aquí según sea necesario
    path('registro/', registro_usuario, name='registro'),
]

