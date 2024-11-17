from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Genero, Director

def index(request):
    peliculas = Pelicula.objects.all()
    peliculas_recientes = {}

    for pelicula in peliculas:
        genero=pelicula.genero
        if genero:  # Verifica que la película tenga un género
            if genero not in peliculas_recientes:
                peliculas_recientes[genero] = pelicula
            else:
                # Compara fechas de estreno
                if pelicula.fecha_estreno > peliculas_recientes[genero].fecha_estreno:
                    peliculas_recientes[genero] = pelicula
    context = {
        'peliculas_recientes': peliculas_recientes,
    }
    return render(request, 'index.html', context)

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'movie_list.html', {'peliculas': peliculas})

def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    return render(request, 'movie_detail.html', {'pelicula': pelicula})

def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'genre_list.html', {'generos': generos})

def detalle_genero(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)
    return render(request, 'genre_detail.html', {'genero': genero})

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'director_list.html', {'directores': directores})

def detalle_director(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    return render(request, 'director_detail.html', {'director': director})
