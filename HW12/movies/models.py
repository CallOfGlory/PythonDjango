from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    director = models.CharField(max_length=200, verbose_name='Режисер')
    release_date = models.DateField(verbose_name='Дата випуску')
    description = models.TextField(blank=True, verbose_name='Опис')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг (1-5)',
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