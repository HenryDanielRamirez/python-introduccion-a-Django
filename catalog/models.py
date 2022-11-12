import uuid

from django.db import models

# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del Genero")

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=300, help_text="Intruduce de que trata la Pelicula")
    genre = models.ManyToManyField(Genre)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])


class FilmIntance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para esta pelicula")
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    def __str__(self):
        return '%s, %s' %(self.last_name, self.first_name)

