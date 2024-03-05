from django.shortcuts import render
from clientes.models import Clientes

# Create your views here.
def listarClientes(request):
    listado_clientes = Clientes.objects.all()
    contexto = {'clientes': listado_clientes}
    return render(request,'listado_clientes.html',context=contexto)