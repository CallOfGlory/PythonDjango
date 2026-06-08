from django.db import models


class Actor(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    biography = models.TextField(blank=True)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=200)
    release_year = models.IntegerField()
    duration = models.IntegerField(help_text='Тривалість у хвилинах')
    studio = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_actors')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movie_roles')
    role = models.CharField(max_length=200)

    class Meta:
        unique_together = ('movie', 'actor', 'role')

    def __str__(self):
        return f"{self.actor.full_name} as {self.role} in {self.movie.title}"
