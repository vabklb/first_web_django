from django.db import models

# Create your models here.

class Categoria_producto(models.Model):
    nombre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'categoria_prod'
        verbose_name_plural = 'categorias_prod'
    
    def __str__(self):
        return self.nombre

    


class Producto(models.Model): 
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    categorias = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda', null= True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.nombre