from rest_framework import serializers
from .models import Course, CustomUser, Document, Notification, Profile, Resource

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'level', 'department', 'email', 'matricno', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            matricno=validated_data['matricno'],
            phonenumber=validated_data['level'],
            email=validated_data['email'],
            department=validated_data['department'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    registered_courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user',
            'registered_courses',
            'total_units',
            'level',
            'phone_number',
            'about',
            'department',
            'matric_number',
        ]

