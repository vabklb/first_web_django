from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'blogApp/home.html')
    
def servicios(request):
    return render(request, 'blogApp/servicios.html')

def tienda(request):
    return render(request, 'blogApp/tienda.html')

def blog(request):
    return render(request, 'blogApp/blog.html')

def contacto(request):
    return render(request, 'blogApp/contacto.html')