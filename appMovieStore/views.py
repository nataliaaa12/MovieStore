from django.views.generic import ListView, DetailView
from .models import Pelicula, Genero, Director
from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404

from .forms import PeliculaForm 

def pelicula_form_view(request):
    pelicula_form = PeliculaForm()
    return render(request, 'movie_detail.html', {'form': pelicula_form})


def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'movie_detail.html', {'form': form, 'titulo_pagina': 'Crear Nueva Película'})



class IndexView(ListView):
    model = Pelicula
    template_name = 'index.html'
    context_object_name = 'peliculas_recientes'

    def get_queryset(self):
        # Obtenemos todas las películas
        peliculas = get_list_or_404(Pelicula.objects.all())

        # Diccionario para almacenar la película más reciente por género
        peliculas_recientes = {}

        # Filtramos las películas más recientes por género
        for pelicula in peliculas:
            genero = pelicula.genero
            if genero:
                if genero not in peliculas_recientes:
                    peliculas_recientes[genero] = pelicula
                elif pelicula.fecha_estreno > peliculas_recientes[genero].fecha_estreno:
                    peliculas_recientes[genero] = pelicula

        # Convertimos el diccionario a una lista de películas
        # Esto devuelve solo las películas más recientes por género
        return list(peliculas_recientes.values())
    

class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'movie_list.html'
    context_object_name = 'peliculas'

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'movie_detail.html'
    context_object_name = 'pelicula'

class GeneroListView(ListView):
    model = Genero
    template_name = 'genre_list.html'
    context_object_name = 'generos'

class GeneroDetailView(DetailView):
    model = Genero
    template_name = 'genre_detail.html'
    context_object_name = 'genero'

class DirectorListView(ListView):
    model = Director
    template_name = 'director_list.html'
    context_object_name = 'directores'

class DirectorDetailView(DetailView):
    model = Director
    template_name = 'director_detail.html'
    context_object_name = 'director'
