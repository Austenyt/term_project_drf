from rest_framework import serializers
from .models import Habit
from .validators import RewardOrRelatedHabitValidator, DurationValidator, RelatedHabitValidator, EnjoyedHabitValidator, \
    FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardOrRelatedHabitValidator(),
            DurationValidator(),
            RelatedHabitValidator(),
            EnjoyedHabitValidator(),
            FrequencyValidator(),
        ]
