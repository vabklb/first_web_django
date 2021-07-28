from django.shortcuts import render, redirect
from .forms import forms_contacto
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.

def contacto(request):
    formulario = forms_contacto()

    if request.method == 'POST':
        formulario = forms_contacto(data=request.POST)
        if formulario.is_valid():
            email = request.POST.get('email')
            nombre = request.POST.get('nombre')
            mensaje = request.POST.get('mensaje')
            
            email = EmailMessage(
                'Mensaje desde app django',
                'El usuario {} escribe:\n\n {} \n\n Correo electronico de {}: {} '.format(nombre, mensaje, nombre, email),
                '',
                [settings.EMAIL_HOST_USER],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect ('/contacto/?valido')
            except:
                return redirect ('/contacto/?fallido')

    return render(request, 'contacto/contacto.html', {'formulario':formulario})