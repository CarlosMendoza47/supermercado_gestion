from django.urls import path
from .views import login_view, logout_view, inicio

urlpatterns = [
    path('', login_view, name='login'),      # Página de inicio
    path('login/', login_view, name='login'),
    path('inicio/', inicio, name='inicio'),
    path('logout/', logout_view, name='logout'),
]

