from django.contrib import admin
from .models import Genre, Filmwork, GenreFilmwork, Person


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline,)

    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created', 'modified')

