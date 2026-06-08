from django.db import models


class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Робота', 'Робота'),
        ('Здоров\'я', 'Здоров\'я'),
        ('Їжа', 'Їжа'),
        ('Відпочинок', 'Відпочинок'),
        ('Навчання', 'Навчання'),
        ('Інше', 'Інше'),
    ]

    title = models.CharField(max_length=200, verbose_name='Назва завдання')
    time = models.TimeField(verbose_name='Час виконання')
    completed = models.BooleanField(default=False, verbose_name='Виконано')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='Категорія')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time']
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'

    def __str__(self):
        return f"{self.time.strftime('%H:%M')} - {self.title}"
