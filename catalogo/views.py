from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
	Libros = Libro.objects.all() 
	context = {
       "Libros": Libros
    }
	return render (request, 'catalogo/index.html', context)

def categoria_libros(request):
	Libros = Libro.objects.all() 
	context = {
       "Libros": Libros
    }
	return render (request, 'catalogo/categoria_libros.html', context)

def categoria_autores(request):
	Autores = Autor.objects.all() 
	context = {
       "Autores": Autores
    }
	return render (request, 'catalogo/categoria_autores.html', context)

def pagina_categorias(request):
	Categorias = Categoria.objects.all() 
	context = {
       "Categorias": Categorias
    }
	return render (request, 'catalogo/pagina_categorias.html', context)
