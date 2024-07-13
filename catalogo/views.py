from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
import json

# Create your views here.

def index(request):
	Navbars = Navbar.objects.all()
	context = {
     	"Navbars": Navbars,
    }
	return render (request, 'catalogo/index.html', context)

def categoria_libros(request):
	Navbars = Navbar.objects.all()
	Libros = Libro.objects.all() 
	context = {
    	"Navbars": Navbars,
       	"Libros": Libros
    }
	return render (request, 'catalogo/categoria_libros.html', context)

def categoria_autores(request):
	Navbars = Navbar.objects.all()
	Autores = Autor.objects.all() 
	context = {
		"Navbars": Navbars,
      	"Autores": Autores
    }
	return render (request, 'catalogo/categoria_autores.html', context)

def pagina_categorias(request):
	Navbars = Navbar.objects.all()
	Categorias = Categoria.objects.all() 
	context = {
		"Navbars": Navbars,
       	"Categorias": Categorias
    }
	return render (request, 'catalogo/pagina_categorias.html', context)

def display_images(request):
    return render(request, 'myapp/display_images.html')

def display_video(request):
    return render(request, 'myapp/display_video.html')

