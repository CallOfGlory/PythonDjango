from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва задачі')
    description = models.TextField(blank=True, verbose_name='Опис')
    completed = models.BooleanField(default=False, verbose_name='Виконано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    deadline = models.DateField(null=True, blank=True, verbose_name='Дедлайн')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'

    def __str__(self):
        return self.title