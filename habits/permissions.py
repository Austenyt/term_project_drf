from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Право доступа, разрешающее только владельцу объекта редактирование его данных.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено чтение для всех запросов
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешено редактирование только владельцу привычки
        return obj.user == request.user


class ReadOnlyPublicHabit(permissions.BasePermission):
    """
    Право доступа, разрешающее только чтение публичных привычек.
    """

    def has_permission(self, request, view):
        # Разрешено чтение для всех запросов
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Разрешено чтение только публичных привычек
        return obj.is_public
