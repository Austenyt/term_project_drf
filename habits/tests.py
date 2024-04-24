import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        """Создается тестовый пользователь"""
        self.user = User.objects.create(email='test@test.pro')
        self.user.set_password('qwe12345')
        self.user.save()

        """Аутентификация пользователя"""

        self.client.force_authenticate(user=self.user)

        """Создается тестовая привычка"""

        self.habit = Habit.objects.create(
            user=self.user,
            place='Работа',
            time='08:00:00',
            action='Работать',
            is_enjoyed=False,
            frequency=5,
            reward='Вознаграждение',
            lasting=110,
            is_public=True,
        )

    def test_habit_create(self):
        data = {
            'user': self.user.id,
            'place': 'Дом',
            'time': '18:00:00',
            'action': 'Отдыхать',
            'is_enjoyed': True,
            'frequency': 5,
            'reward': 'Сон',
            'lasting': 105,
            'is_public': True,
        }
        response = self.client.post(reverse('habits:habit_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_list(self):
        response = self.client.get(reverse('habits:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'count': 1,
                             'next': None,
                             'previous': None,
                             'results': [
                                 {
                                     'id': self.habit.id,
                                     'user': self.habit.user.id,
                                     'place': self.habit.place,
                                     'time': self.habit.time,
                                     'action': self.habit.action,
                                     'is_enjoyed': self.habit.is_enjoyed,
                                     'related_habit': self.habit.related_habit,
                                     'reward': self.habit.reward,
                                     'lasting': self.habit.lasting,
                                     'is_public': self.habit.is_public,
                                     'frequency': self.habit.frequency,

                                 }
                             ]
                         })

    def test_public_habit_list(self):
        response = self.client.get(reverse('habits:habit_public'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'count': 1,
                             'next': None,
                             'previous': None,
                             'results': [
                                 {
                                     'id': self.habit.id,
                                     'user': self.habit.user.id,
                                     'place': self.habit.place,
                                     'time': self.habit.time,
                                     'action': self.habit.action,
                                     'is_enjoyed': self.habit.is_enjoyed,
                                     'related_habit': self.habit.related_habit,
                                     'reward': self.habit.reward,
                                     'lasting': self.habit.lasting,
                                     'is_public': self.habit.is_public,
                                     'frequency': self.habit.frequency,

                                 }
                             ]
                         })

    def test_habit_detail(self):
        response = self.client.get(reverse('habits:habit_detail', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'id': self.habit.id,
                             'user': self.habit.user.id,
                             'place': self.habit.place,
                             'time': self.habit.time,
                             'action': self.habit.action,
                             'is_enjoyed': self.habit.is_enjoyed,
                             'related_habit': self.habit.related_habit,
                             'reward': self.habit.reward,
                             'lasting': self.habit.lasting,
                             'is_public': self.habit.is_public,
                             'frequency': self.habit.frequency,
                         })

    def test_habit_update(self):
        data = {
            'place': 'Клуб',
            'time': '23:00:00',
            'action': 'Зажигать',
            'is_enjoyed': True,
            'frequency': 1,
            'lasting': 119,
            'is_public': True,
        }
        response = self.client.put(reverse('habits:habit_update', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'id': self.habit.id,
                             'user': self.habit.user.id,
                             'place': data['place'],
                             'time': data['time'],
                             'action': data['action'],
                             'is_enjoyed': data['is_enjoyed'],
                             'related_habit': self.habit.related_habit,
                             'reward': self.habit.reward,
                             'lasting': data['lasting'],
                             'is_public': data['is_public'],
                             'frequency': data['frequency'],
                         })

    def test_habit_destroy(self):
        response = self.client.delete(reverse('habits:habit_delete', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_habit_validation(self):
        data = {
            'user': self.user.id,
            'place': 'Где-нибудь',
            'time': '03:00:00',
            'action': 'Что-нибудь',
            'is_enjoyed': True,
            'frequency': 1,
            'reward': 'Всё, что угодно',
            'lasting': 130,
            'is_public': True,
        }
        response = self.client.post(reverse('habits:habit_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Время выполнения привычки не должно быть больше 120 секунд",
                                 "У приятной привычки не может быть вознаграждения или связанной привычки"
                             ]
                         })
