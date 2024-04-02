from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Evento

def eventos(request):
    eventos = Evento.objects.all().order_by('fecha')
    contexto = {'eventos':eventos}
    return render(request, 'eventos/eventos.html', contexto)


def evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    related_eventos = Evento.objects.all().order_by('fecha')
    contexto = {'evento':evento, 'related_eventos':related_eventos}

    return render(request, 'eventos/evento.html', contexto)