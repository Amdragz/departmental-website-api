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
        user_id = self.kwargs['user_id']
        return CustomUser.objects.get(user_id=user_id)
    
class DocumentViewSet(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

class CourseViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class ResourceViewSet(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]

class NotificationViewSet(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

# class ProfileViewSet(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer