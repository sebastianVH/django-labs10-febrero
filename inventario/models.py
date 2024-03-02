from typing import Any
from django.db import models

# Create your models here.
''' 
Crear nuestras TABLAS pero basadas en class:
voy a crear una class que represente UNA TABLA y darle los ATRIBUTOS que van a representar los CAMPOS

la tabla se llamara Productos, y tendra los campos nombre_producto , precio_producto, stock_producto.
Esto lo pasara a una class

'''
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=30, null=False) # dato: string: restriccion max_length nos dice que el campo no puede tener mas de 30 caracteres, y null=False nos dice que NO PUEDE ESTAR VACIO
    precio_producto = models.FloatField() # dato: float
    stock_producto = models.IntegerField(default=0) # dato: integer. cuando vayamos a crearlo, si no podemos un stock, automaticamente se completa en 0
    fecha_creacion = models.TimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nombre_producto
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'