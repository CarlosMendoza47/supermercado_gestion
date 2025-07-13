from django.urls import path
from .views import CustomLoginView, CustomLogoutView, inicio

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('inicio/', inicio, name='inicio'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
