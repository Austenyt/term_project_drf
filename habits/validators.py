from rest_framework.exceptions import ValidationError


class RewardOrRelatedHabitValidator:
    def __call__(self, value):
        if value.reward and value.related_habit:
            raise ValidationError("Награда и связанная привычка не могут быть заданы одновременно.")


class ExecutionTimeValidator:
    def __call__(self, value):
        if value.execution_time > 120:
            raise ValidationError("Время выполнения не может превышать 120 секунд.")


class RelatedHabitValidator:
    def __call__(self, value):
        if value.related_habit and not value.related_habit.is_pleasant_habit:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


class PleasantHabitValidator:
    def __call__(self, value):
        if value.is_pleasant_habit and (value.reward or value.related_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class PeriodicityValidator:
    def __call__(self, value):
        if value.periodicity < 1:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
