from django.db import models
from django.contrib.auth.models import User

from config import settings


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', null=True,
                             blank=True)
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_enjoyed = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', null=True,
                                      blank=True)
    periodicity = models.IntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=255, verbose_name='Вознаграждение', null=True,
                              blank=True)
    execution_time = models.IntegerField(verbose_name='Время на выполнение', null=True, blank=True)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.action} - {self.time}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
