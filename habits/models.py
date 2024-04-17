from django.db import models
from config import settings


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', null=True,
                             blank=True)
    place = models.CharField(max_length=150, verbose_name='Место выполнения')
    date = models.DateField(verbose_name='Дата выполнения')
    time = models.TimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_enjoyed = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', null=True,
                                      blank=True)
    frequency = models.PositiveIntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=255, verbose_name='Вознаграждение', null=True,
                              blank=True)
    duration = models.PositiveIntegerField(verbose_name='Время на выполнение', null=True, blank=True)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'Я, {self.user} буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
