from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'