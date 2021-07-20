from django.shortcuts import render

from .models import Servicios

# Create your views here.

def servicios(request):
    servis = Servicios.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servis})