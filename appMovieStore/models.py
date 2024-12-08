from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # Breve biografía o descripción
    foto = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # Breve biografía o descripción
    mensaje = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='directores/', blank=True, null=True)  # Foto del director 

    def __str__(self):
        return self.nombre

# models.py
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripción')
    duracion = models.IntegerField(verbose_name='Duración')
    fecha_estreno = models.DateField(verbose_name='Fecha estreno')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name='Genero')
    directores = models.ManyToManyField(Director, verbose_name='Directores')
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    trailer = models.URLField(blank=True, null=True)  # Nuevo atributo para el trailer de YouTube


    def __str__(self):
        return self.titulo


