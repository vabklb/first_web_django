from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('categorias/<int:categoria_id>/', views.categoria, name='categorias'),
]