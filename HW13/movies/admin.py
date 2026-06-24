from django.contrib import admin

from .models import Genre, Movie, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director', 'genre', 'release_date', 'rating')
    list_filter = ('rating', 'genre', 'release_date')
    search_fields = ('title', 'director')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'username', 'created_at')
    list_filter = ('movie',)
    search_fields = ('username', 'text')