from django.urls import path
from .views import index, lista_peliculas, detalle_pelicula, lista_generos, detalle_genero, lista_directores, detalle_director

urlpatterns = [
    path('', index, name='index'),
    path('peliculas/', lista_peliculas, name='lista_peliculas'),
    path('peliculas/<int:pelicula_id>/', detalle_pelicula, name='detalle_pelicula'),
    path('generos/', lista_generos, name='lista_generos'),
    path('generos/<int:genero_id>/', detalle_genero, name='detalle_genero'),
    path('directores/', lista_directores, name='lista_directores'),
    path('directores/<int:director_id>/', detalle_director, name='detalle_director'),
]

