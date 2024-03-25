from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователя"""

    username = None

    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=25, **NULLABLE, verbose_name='Телефон')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Город')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Аватар')
    is_active = models.BooleanField(default=False, verbose_name='Активность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
