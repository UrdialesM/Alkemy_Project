from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('lista_proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('', TemplateView.as_view(template_name='base/index.html'), name='index'),
]