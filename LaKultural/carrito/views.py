from django.shortcuts import render

def carrito(request):
    contexto = {'mensaje': "Hola, mundo. Este es mi contexto."}
    return render(request, 'carrito/carrito.html', contexto)