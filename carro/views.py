from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto
# Create your views here.

def agregar_producto (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.add(producto=producto)
    return redirect('tienda')

def eliminar_producto (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.dell(producto=producto)
    return redirect('tienda')

def restar_producto (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.dell_unidad(producto=producto)
    return redirect('tienda')

def limpiar_carro(request):
    carro = Carro(request)
    carro.clean()
    return redirect('tienda')