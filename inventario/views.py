from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
from inventario.models import Productos, Categorias

# Create your views here.
#Creamos LOS CONTROLADORES para administrar nuestra LOGICA, y nuestras VISTAS

def listarProductos(request):
    #deberia devolver EL LISTADO DE LOS PRODUCTOS:
    lista_productos = Productos.objects.all() #Del Modelo Productos, traigo TODOS los objetos
    lista_categorias = Categorias.objects.all()
    #crearemos un CONTEXTO: un diccionario que mediante UNA LLAVE (que sera la que se mostrara y usara en el HTML) y un valor (pondremos LO QUE QUERRAMOS ENVIARLE) nos permitira ENIVAR Y RENDERIZAR DATOS
    contexto = {'productos':lista_productos,'categorias': lista_categorias}
    return render(request,'listado.html', context=contexto)

def crearProducto(request):
    #capturo LOS name que provienen de los input, desde la request
    nombre = request.POST['nombre'].capitalize()
    precio = request.POST['precio']
    stock = request.POST['stock']
    categoria_fk = request.POST['categoria']
    #Buscar la CATEGORIA que pertenezca al NUMERO proveniente del POST e INSTANCIARLA
    categoria = Categorias.objects.get(id=categoria_fk)
    #creo mi objeto nuevo de un producto, usando la class Productos
    producto = Productos(nombre_producto=nombre,precio_producto=precio, stock_producto=stock,categoria_fk=categoria)
    #debo almacenarlo, usando un metodo
    producto.save()
    return redirect('listado_productos')

def editarProducto(request,id):
    #buscando el producto para EDITAR
    #producto_a_editar = Productos.objects.get(id=id)
    try:
        producto_a_editar = get_object_or_404(Productos,id=id)
        lista_categorias = Categorias.objects.all()
    except Http404:
        return render(request,'error.html')
    
    if request.method == 'GET':
        contexto = {'producto':producto_a_editar,'categorias': lista_categorias}
        return render(request,'editar_producto.html',contexto)
    
    elif request.method == 'POST':
        #capturo los datos
        nombre_nuevo = request.POST['nombre']
        precio_nuevo = request.POST['precio']
        stock_nuevo = request.POST['stock']
        categoria_id = request.POST['categoria']
        categoria_nueva = Categorias.objects.get(id=categoria_id)
        #actualizo cada campo del objeto a editar
        producto_a_editar.nombre_producto = nombre_nuevo
        producto_a_editar.precio_producto = precio_nuevo
        producto_a_editar.stock_producto = stock_nuevo
        producto_a_editar.categoria_fk = categoria_nueva
        #ALMACENAMOS LOS CAMBIOS
        producto_a_editar.save()
        return redirect('listado_productos')
    
def eliminarProducto(request,id):
    #buscar cual es el producto que quiero eliminar!
    try:
        producto_a_eliminar = get_object_or_404(Productos,id=id)
    except Http404:
        return render(request,'error.html')
    producto_a_eliminar.delete()
    return redirect('listado_productos')

def crearCategoria(request):
    #Capturar el NOMBRE de la CATEGORIA proveniente del POST
    nombre = request.POST['nombre_categoria'].capitalize()
    #Crear un nuevo Objeto desde la clase Categorias
    categoria = Categorias(nombre_categoria=nombre)
    categoria.save()
    return redirect('listado_productos')