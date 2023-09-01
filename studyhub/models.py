from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    image = models.ImageField(upload_to='courses/', verbose_name='Изображение курса', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    image = models.ImageField(upload_to='lessons/', verbose_name='Изображение урока', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    video = models.URLField(verbose_name='Видео', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
