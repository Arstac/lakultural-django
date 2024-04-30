from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from eventos.models import Evento
from booking.models import Artista
from tienda.models import Producto


def home(request):
    contexto = {'mensaje': "Hola, mundo. Este es mi contexto."}
    return render(request, 'core/home.html', contexto)



def buscar(request):
    if request.is_ajax():
        query = request.GET.get('term', '')  # 'term' será lo que el usuario está escribiendo
        eventos = Evento.objects.filter(nombre__icontains=query)
        artistas = Artista.objects.filter(nombre__icontains=query)
        productos = Producto.objects.filter(nombre__icontains=query)
        results = []
        for evento in eventos:
            results.append(evento.nombre)
        for artista in artistas:
            results.append(artista.nombre)
        for producto in productos:
            results.append(producto.nombre)
        data = {
            'list': results
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Error: no se realizó una solicitud AJAX"}, status=400)