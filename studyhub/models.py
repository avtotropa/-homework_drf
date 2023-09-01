from django.utils import timezone

from django.db import models
from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    image = models.ImageField(upload_to='courses/', verbose_name='Изображение курса', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

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
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    CASH = 'cash'
    TRANSFER = 'transfer'

    PAYMENT_METHOD_CHOICES = (
        (TRANSFER, 'Карта'),
        (CASH, 'Наличными'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    date_of_payment = models.DateTimeField(default=timezone.now, verbose_name='Дата платежа')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма платежа')
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, default=TRANSFER, verbose_name='Метод платежа', )
    payment_intent_id = models.CharField(max_length=100, verbose_name='ID платежа Stripe', **NULLABLE)

    def __str__(self):
        if self.paid_lesson:
            return f'Платеж на сумму {self.payment_amount} курса {self.paid_course}'
        else:
            return f'Платеж на сумму {self.payment_amount} урока {self.paid_lesson}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
