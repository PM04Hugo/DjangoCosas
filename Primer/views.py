from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def saludo(request):
    return HttpResponse("Hola Mundo") 

def libros(request):
    datos_libros = {
        'nombre': 'El señor de los anillos',
        'autor': 'J.R.R. Tolkien',
    }
    return render(request, 'libros/libros.html', datos_libros)

def enSistema(request):
    return redirect('/libros/')