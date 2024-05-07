from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from tienda.models import Producto
from .models import Carrito, ItemCarrito

def carrito(request):
    #selecciona solo los 2 primeros productos si existen:
    productos = Producto.objects.all()
    productos = productos[:2]
    try:
        carrito = Carrito.objects.get(usuario=request.user)
        items = carrito.items.all()
    except Carrito.DoesNotExist:
        items = []
    return render(request, 'carrito/carrito.html', {'carrito': carrito,
                                                    'items': items,
                                                    'productos': productos})

def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad += 1
    item.save()
    return redirect('carrito:carrito')

def quitar_producto(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()
    return redirect('carrito:carrito')

def checkout(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = carrito.items.all()
    total = carrito.total_carrito()
    return render(request, 'carrito/checkout.html', {'carrito': carrito,
                                                    'items': items,
                                                    'total': total})



def update_item_quantity(request, item_id, product_id, quantity):
    item = get_object_or_404(ItemCarrito, id=item_id, producto_id=product_id)
    item.cantidad = int(quantity)
    item.save()
    
    carrito = item.carrito
    total_carrito = sum(item.subtotal() for item in carrito.items.all())
    
    return JsonResponse({
        'subtotal': item.subtotal(),
        'total_carrito': total_carrito
    })