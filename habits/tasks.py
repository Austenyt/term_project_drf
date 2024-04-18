import datetime
import requests
from celery import shared_task
from django.conf import settings
from django.utils import timezone
from habits.models import Habit


@shared_task
def habit_scheduler():
    habits = Habit.objects.all()
    for habit in habits:
        now = datetime.datetime.now()
        now = timezone.make_aware(now, timezone.get_current_timezone())
        if not habit.is_enjoyed and now.hour == habit.time.hour and now.minute == habit.time.minute:
            text = f"Я буду {habit.action} в {habit.time.strftime('%H:%M')} в {habit.place}"
            user_chat_id = habit.user.chat_id  # Получаем chat_id пользователя из модели User
            send_message(text, user_chat_id)  # Отправляем сообщение с использованием числового chat_id

            if habit.associated_hab:
                text = f"Затем я сделаю: {habit.associated_hab}"
                send_message(text, user_chat_id)
            elif habit.reward:
                text = f"Я получу: {habit.reward}"
                send_message(text, user_chat_id)


def send_message(text, user_chat_id):
    url = 'https://api.telegram.org/bot'
    token = settings.TELEGRAM_TOKEN
    requests.post(
        url=f"{url}{token}/sendMessage",
        data={
            "chat_id": user_chat_id,
            "text": text
        }
    )
