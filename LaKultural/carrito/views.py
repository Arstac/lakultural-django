from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from tienda.models import Producto
from .utils import get_carrito_or_create

def carrito(request):
    carrito = get_carrito_or_create(request)
    contexto = {'carrito': carrito}
    return render(request, 'carrito/carrito.html', contexto)

def add_producto(request, producto_id):
    carrito = get_carrito_or_create(request)
    producto = get_object_or_404(Producto, id=producto_id)

    carrito.productos.add(producto)
    return render(request, 'carrito/carrito.html', {'carrito': carrito})

def remove_producto(request, producto_id):
    carrito = get_carrito_or_create(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.productos.remove(producto)
    return render(request, 'carrito/carrito.html', {'carrito': carrito})
