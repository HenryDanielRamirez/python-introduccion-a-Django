from django.contrib import admin

# Register your models here.
from .models import Genre,Film, FilmIntance, Author

admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(FilmIntance)
admin.site.register(Author)