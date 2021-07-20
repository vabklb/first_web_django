from django.contrib import admin
from .models import Categoria, Post
# Register your models here.

class Categoria_admin(admin.ModelAdmin):
    readonly_fields=('created','update')

class Post_admin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(Post, Post_admin)
admin.site.register(Categoria, Categoria_admin)
