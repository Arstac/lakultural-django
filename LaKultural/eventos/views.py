from django.shortcuts import render
from .models import Evento

def eventos(request):
    eventos = Evento.objects.all()
    contexto = {'eventos':eventos}
    return render(request, 'eventos/eventos.html', contexto)