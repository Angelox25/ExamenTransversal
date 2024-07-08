from django.urls import path, include
from . import views

urlpatterns = [
	path('index', views.index, name="index"),
	path('categoria_libros', views.categoria_libros, name="categoria_libros"),
	path('categoria_autores', views.categoria_autores, name="categoria_autores"),
	path('pagina_categorias', views.pagina_categorias, name="pagina_categorias"),
 
]
