from rest_framework import generics
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from .models import CustomUser

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
