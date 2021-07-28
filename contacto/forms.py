from django import forms

class forms_contacto(forms.Form):
    email = forms.EmailField(label='email', required = True, max_length='50')
    nombre = forms.CharField(label='nombre', required = True, max_length='50')
    mensaje = forms.CharField(label='mensaje', required=True, widget=forms.Textarea, max_length='400' )