from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'blogApp/home.html')

def tienda(request):
    return render(request, 'blogApp/tienda.html')

def contacto(request):
    return render(request, 'blogApp/contacto.html')