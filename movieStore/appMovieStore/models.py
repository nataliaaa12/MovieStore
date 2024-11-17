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
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    fecha_estreno = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    directores = models.ManyToManyField(Director)
    portada = models.ImageField(upload_to='portadas/')
    trailer = models.URLField(blank=True, null=True)  # Nuevo atributo para el trailer de YouTube


    def __str__(self):
        return self.titulo


