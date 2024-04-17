from django.utils import timezone
from rest_framework.exceptions import ValidationError


class RewardOrRelatedHabitValidator:
    def __call__(self, value):
        if value.reward and value.related_habit:
            raise ValidationError("Награда и связанная привычка не могут быть заданы одновременно.")


class DurationValidator:
    def __call__(self, value):
        if value.execution_time > 120:
            raise ValidationError("Время выполнения не может превышать 120 секунд.")


class RelatedHabitValidator:
    def __call__(self, value):
        if value.related_habit and not value.related_habit.is_enjoyed:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


class EnjoyedHabitValidator:
    def __call__(self, value):
        if value.is_enjoyed and (value.reward or value.related_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class FrequencyValidator:
    def __call__(self, value):
        # Проверяем, что хотя бы одно выполнение привычки за неделю
        one_week_ago = timezone.now() - timezone.timedelta(days=7)
        if not value.date.filter(date__gte=one_week_ago).exists():
            raise ValidationError("Необходимо выполнить привычку хотя бы один раз за неделю.")
