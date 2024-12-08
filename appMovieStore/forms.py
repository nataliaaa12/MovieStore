from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'duracion', 'fecha_estreno', 'genero', 'directores', 'portada', 'trailer']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'fecha_estreno': forms.SelectDateWidget(years=range(1900, 2025)),
        }