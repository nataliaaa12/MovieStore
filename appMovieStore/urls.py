from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    IndexView,
    PeliculaListView,
    PeliculaDetailView,
    GeneroListView,
    GeneroDetailView,
    DirectorListView,
    DirectorDetailView,
    crear_pelicula,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Página de inicio
    path('peliculas/', PeliculaListView.as_view(), name='lista_peliculas'),  # Lista de películas
    path('peliculas/<int:pk>/', PeliculaDetailView.as_view(), name='detalle_pelicula'),  # Detalle de película
    path('generos/', GeneroListView.as_view(), name='lista_generos'),  # Lista de géneros
    path('generos/<int:pk>/', GeneroDetailView.as_view(), name='detalle_genero'),  # Detalle de género
    path('directores/', DirectorListView.as_view(), name='lista_directores'),  # Lista de directores
    path('directores/<int:pk>/', DirectorDetailView.as_view(), name='detalle_director'),  # Detalle de director
    path('peliculas/nueva/', crear_pelicula, name='crear_pelicula'),  #formulario
]

if settings.DEBUG:  # Esto asegura que solo se carguen archivos de medios en modo DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

