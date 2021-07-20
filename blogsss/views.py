from django.shortcuts import render
from .models import Post, Categoria
# Create your views here.

def blog(request):
    post = Post.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'blog/blog.html', {'post': post, 'categoria': categoria})