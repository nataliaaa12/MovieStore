# Generated by Django 5.1.2 on 2024-11-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMovieStore', '0007_director_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(default=0.0006737333812432626),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(upload_to='portadas/'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
