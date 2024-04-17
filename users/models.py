from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True)
    chat_id = models.TextField(verbose_name='id чата в телеге', null=True, blank=True)
    telegram_user_name = models.CharField(max_length=200, verbose_name='имя в телеге', unique=True, null=True,
                                          blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
