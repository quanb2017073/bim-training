from rest_framework import serializers
from .models import UserRole, UserType, VIPStatus, CustomUser

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = (
            'role_name',
        )
        
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = (
            'type_name',
        )
        
class VIPStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIPStatus
        fields = (
            'VIP_status_name',
        )
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'