from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('index', views.index, name="index"),
	path('categoria_libros', views.categoria_libros, name="categoria_libros"),
	path('categoria_autores', views.categoria_autores, name="categoria_autores"),
	path('pagina_categorias', views.pagina_categorias, name="pagina_categorias"),
 
	path('display-images/', views.display_images, name='display_images'),
    path('display-video/', views.display_video, name='display_video'),
    
    path('get-urls/', views.get_urls, name='get_urls'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
