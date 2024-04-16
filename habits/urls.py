from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, PublicHabitListView

router = DefaultRouter()
router.register(r'habits', HabitViewSet)
urlpatterns = [
    path('public-habits/', PublicHabitListView.as_view()),
]
urlpatterns += router.urls
