from django.shortcuts import render, redirect
from .forms import ProductoForm, ProveedorForm
from .models import Producto, Proveedor

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})


def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()

    return render(request, 'agregar_proveedor.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})
