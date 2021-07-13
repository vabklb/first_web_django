from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('servicios/', views.servicios, name='servicios'),
    path('tienda/', views.tienda, name='tienda'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
]