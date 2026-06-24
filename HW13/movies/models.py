from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Назва жанру')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    director = models.CharField(max_length=200, verbose_name='Режисер')
    release_date = models.DateField(verbose_name='Дата випуску')
    description = models.TextField(blank=True, verbose_name='Опис')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг (1-5)',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies',
        verbose_name='Жанр',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Додано')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name='movie_rating_1_to_5',
            ),
        ]

    def __str__(self):
        return f'{self.title} ({self.release_date.year})'


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Фільм',
    )
    username = models.CharField(max_length=80, verbose_name='Ім\'я користувача')
    text = models.TextField(verbose_name='Текст відгуку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f'{self.username}: {self.text[:40]}'