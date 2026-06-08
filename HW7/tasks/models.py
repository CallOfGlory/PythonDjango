from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок задачі")
    description = models.TextField(verbose_name="Текст задачі")
    start_date = models.DateTimeField(verbose_name="Дата початку")
    end_date = models.DateTimeField(verbose_name="Дата завершення")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачі"
        ordering = ['-created_at']
