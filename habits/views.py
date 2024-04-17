from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from habits.permissions import IsOwnerOrReadOnly, ReadOnlyPublicHabit
from .models import Habit
from .paginators import HabitPagination
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsOwnerOrReadOnly | ReadOnlyPublicHabit]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserHabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
