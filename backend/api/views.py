from rest_framework import generics
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class GetUserByMatricNoView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        matricno = self.kwargs['matricno']
        return CustomUser.objects.get(matricno=matricno)