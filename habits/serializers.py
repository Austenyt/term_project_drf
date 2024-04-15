from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'is_pleasurable', 'related_habit', 'frequency', 'reward',
                  'time_required', 'is_public')
