from django.db import models

# Create your models here.

class Libro(models.Model):
    id_libro = models.AutoField(db_column="idLibro", primary_key=True)
    titulo = models.CharField(max_length=20, blank=False, null=False)
    anio = models.IntegerField()
    descripcion_libro = models.CharField(max_length=255, blank=False, null=False)

class Autor(models.Model):
    id_autor = models.AutoField(db_column="idAutor", primary_key=True)
    nombre_autor = models.CharField(max_length=255, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column="idCategoria", primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    descripcion_categoria = models.CharField(max_length=255)

class Navbar(models.Model):
    id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre