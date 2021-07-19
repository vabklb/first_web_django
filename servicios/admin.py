from django.contrib import admin
from .models import Servicios

# Register your models here.

class Servicios_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Servicios, Servicios_admin)