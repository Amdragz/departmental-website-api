from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'phonenumber', 'department', 'email', 'matricno', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            matricno=validated_data['matricno'],
            phonenumber=validated_data['phonenumber'],
            email=validated_data['email'],
            department=validated_data['department'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
