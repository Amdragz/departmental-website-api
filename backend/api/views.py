from rest_framework import generics
from .serializers import CustomUserSerializer, DocumentSerializer, CourseSerializer, ResourceSerializer, NotificationSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser, Document, Course, Resource, Notification, Profile

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
    
class DocumentViewSet(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class CourseViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ResourceViewSet(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class NotificationViewSet(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# class ProfileViewSet(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer