# Generated by Django 5.1.2 on 2024-11-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMovieStore', '0005_director_descripcion_director_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
