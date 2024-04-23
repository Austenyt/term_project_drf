from rest_framework import serializers
from .models import Habit
from .validators import RewardOrRelatedHabitValidator, LastingValidator, RelatedHabitValidator, EnjoyedHabitValidator, \
    FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardOrRelatedHabitValidator(reward='reward', habit='related_habit'),
            LastingValidator(lasting='lasting'),
            RelatedHabitValidator(habit='related_habit'),
            EnjoyedHabitValidator(habit_is_enjoyed='is_enjoyed', reward='reward', habit='related_habit'),
            FrequencyValidator(frequency='frequency'),
        ]
