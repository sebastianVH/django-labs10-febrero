from django.urls import path
from .views import listarClientes

urlpatterns = [
    path('',listarClientes,name='listado_clientes'),
]