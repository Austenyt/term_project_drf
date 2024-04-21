from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class UserRegisterSerializer(serializers.ModelSerializer):
    """Класс сериализатора для регистрации пользователя"""

    class Meta:
        model = User
        fields = ['email', 'password', 'telegram_user_name']
