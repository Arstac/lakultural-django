from django.shortcuts import render

def tienda(request):
    contexto = {'mensaje': "Hola, mundo. Este es mi contexto."}
    return render(request, 'tienda/tienda.html', contexto)