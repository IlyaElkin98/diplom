from django.db import models
from users.models import CustomUser


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название объявления', help_text='Введите названия объявления')
    description = models.TextField(verbose_name='Описание объявления', help_text='Введите описание объявления')
    image = models.ImageField(verbose_name='Фотография объявления')
    date_created = models.DateTimeField(verbose_name='Дата создания объявления')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.description}'


