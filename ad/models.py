from django.db import models
from users.models import CustomUser


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название объявления', help_text='Введите названия объявления')
    description = models.TextField(verbose_name='Описание объявления', help_text='Введите описание объявления')
    images = models.ImageField(verbose_name='Фотография объявления', null=True, blank=True)
    date_created = models.DateTimeField(verbose_name='Дата создания объявления', auto_now=True)
    phone_number = models.CharField(max_length=200, verbose_name='Номер телефона')
    owner = models.ForeignKey(CustomUser, related_name='ad', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.title} - {self.description}'


