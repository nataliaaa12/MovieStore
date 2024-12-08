# Generated by Django 5.1.2 on 2024-12-07 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMovieStore', '0008_pelicula_trailer_alter_pelicula_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='directores',
            field=models.ManyToManyField(to='appMovieStore.director', verbose_name='Directores'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.IntegerField(verbose_name='Duración'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='fecha_estreno',
            field=models.DateField(verbose_name='Fecha estreno'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMovieStore.genero', verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
    ]