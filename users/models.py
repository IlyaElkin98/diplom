from django.contrib.auth.models import AbstractUser
from django.db import models


DISTRICT_CHOICES = [
    ('ce', 'Центральный'),
    ('zh', 'Железнодорожный'),
    ('za', 'Заельцовский'),
    ('ka', 'Калининский'),
    ('ki', 'Кировский'),
    ('le', 'Ленинский'),
    ('oc', 'Октябрьский'),
    ('pe', 'Первомайский'),
    ('so', 'Советский'),
    ('dz', 'Дзержинский'),
]


class CustomUser(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=30,
                                  help_text="Введите своё имя", null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30,
                                 help_text='Введите свою фамилию', null=True, blank=True)
    username = models.CharField(verbose_name='Никнейм', help_text='Введите свой никнейм',
                                max_length=50, unique=True)
    email = models.CharField(verbose_name='Электронная почта',
                             help_text='Введите свою электронную почту', max_length=50)
    date_joined = models.DateField(auto_now_add=True, verbose_name='Дата создания аккаунта')
    avatar = models.ImageField(upload_to='ad/', help_text='Загрузите свой аватар', null=True, blank=True)
    area_of_residence = models.CharField(choices=DISTRICT_CHOICES, verbose_name='Район проживания',
                                         help_text='Выберете район проживания', null=True, blank=True)
    subscription = models.BooleanField(default=False, verbose_name='Признак платной подписки')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.username}'
