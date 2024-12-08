from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from .models import Pelicula, Director, Genero


admin.site.site_header = 'MOVIE VIBES ADMINISTRATION'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Movie Vibes'

class YearFilter(admin.SimpleListFilter):
    title = _('Año de estreno')  # Título del filtro
    parameter_name = 'fecha_estreno'  # Nombre del parámetro en la URL

    def lookups(self, request, model_admin):
        # Genera una lista de años únicos de las fechas de estreno
        years = Pelicula.objects.dates('fecha_estreno', 'year')
        return [(year.year, str(year.year)) for year in years]

    def queryset(self, request, queryset):
        # Filtra el queryset basado en el año seleccionado
        if self.value():
            return queryset.filter(fecha_estreno__year=self.value())
        return queryset

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_estreno', 'duracion')
    ordering = ('titulo',)
    search_fields = ('titulo',)
    list_editable = ('duracion',)
    list_filter = (YearFilter,)
    list_per_page = 6

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    ordering = ('nombre',)
    search_fields = ('nombre',)


class GeneroAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    search_fields = ('nombre',)




# Register your models here.
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genero, GeneroAdmin)