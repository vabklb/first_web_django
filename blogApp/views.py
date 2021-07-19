from django.shortcuts import render, HttpResponse
from servicios.models import Servicios

# Create your views here.

def home(request):
    return render(request, 'blogApp/home.html')
    
def servicios(request):
    servis = Servicios.objects.all()
    return render(request, 'blogApp/servicios.html', {'servicios': servis})

def tienda(request):
    return render(request, 'blogApp/tienda.html')

def blog(request):
    return render(request, 'blogApp/blog.html')

def contacto(request):
    return render(request, 'blogApp/contacto.html')