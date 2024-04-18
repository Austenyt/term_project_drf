from rest_framework.exceptions import ValidationError


class RewardOrRelatedHabitValidator:
    def __init__(self, reward, habit):
        self.reward = reward
        self.habit = habit

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        habit = dict(value).get(self.habit)
        if reward and habit:
            raise ValidationError('Нельзя одновременно выбирать связанную привычку и вознаграждение')


class LastingValidator:
    def __init__(self, lasting):
        self.lasting = lasting

    def __call__(self, value):
        lasting = dict(value).get(self.lasting)
        if lasting > 120:
            raise ValidationError('Время выполнения привычки не должно быть больше 120 секунд')


class RelatedHabitValidator:
    def __init__(self, habit):
        self.habit = habit

    def __call__(self, value):
        if value.get(self.habit):
            is_enjoyed = dict(value).get(self.habit).is_enjoyed
            if not is_enjoyed:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной '
                                      'привычки')


class EnjoyedHabitValidator:
    def __init__(self, enjoyed_habit, reward, habit):
        self.habit_is_enjoyed = enjoyed_habit
        self.reward = reward
        self.habit = habit

    def __call__(self, value):
        enjoyed_habit = dict(value).get(self.enjoyed_habit)
        reward = dict(value).get(self.reward)
        habit = dict(value).get(self.habit)
        if enjoyed_habit:
            if reward or habit:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class FrequencyValidator:
    def __init__(self, frequency):
        self.frequency = frequency

    def __call__(self, value):
        frequency = dict(value).get(self.frequency)
        if frequency < 1:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
