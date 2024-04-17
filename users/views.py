from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
