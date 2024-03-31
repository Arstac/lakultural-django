from django.shortcuts import render

def home(request):
    contexto = {'mensaje': "Hola, mundo. Este es mi contexto."}
    return render(request, 'core/home.html', contexto)