from django.contrib import admin
from .models import Categoria_producto, Producto
# Register your models here.


class Categorias_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Productos_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria_producto, Categorias_admin)
admin.site.register(Producto, Productos_admin)