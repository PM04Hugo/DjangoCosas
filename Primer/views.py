from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola Mundo") 

def libros(request):
    datos_libros = {
        'nombre': 'El señor de los anillos',
        'autor': 'J.R.R. Tolkien',
        'fecha': datetime.now(),
        'valor': 40,
    }
    return render(request, 'libros/libros.html', datos_libros) #Le estoy mandando la info al html, como en admin

def detallelibro(request):
    detalle= {
        'nombreLibro': '''El señor de los anillos, libro de fantasía cuyo autor escribe más lento que la G andando por la calle'''
    }
    return render(request, 'libros/detalle.html', detalle)
    
def enSistema(request):
    return redirect('/libros/')