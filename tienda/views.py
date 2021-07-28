from django.shortcuts import render
from .models import Producto, Categoria_producto
# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    categoria = Categoria_producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos':productos, 'categoria':categoria})

def categoria(request, categoria_id):
    categoria = Categoria_producto.objects.get(id = categoria_id)
    producto = Producto.objects.filter(categorias = categoria)
    return render(request, 'tienda/categorias.html', {'productos':producto, 'categoria':categoria})