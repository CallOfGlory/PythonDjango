from django.contrib import admin
from .models import Movie, Actor, MovieActor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date')
    search_fields = ('full_name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'director', 'release_year', 'studio')
    list_filter = ('genre', 'release_year')
    search_fields = ('title', 'director')


@admin.register(MovieActor)
class MovieActorAdmin(admin.ModelAdmin):
    list_display = ('movie', 'actor', 'role')
    list_filter = ('movie', 'actor')
    search_fields = ('role',)
