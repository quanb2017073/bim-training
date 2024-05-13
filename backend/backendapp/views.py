from django.shortcuts import render
from .models import UserRole, UserType, VIPStatus, CustomUser
from .serializers import UserRoleSerializer, UserTypeSerializer, VIPStatusSerializer, CustomUserSerializer
from rest_framework import viewsets
# Create your views here.

class UserRoleView(viewsets.ModelViewSet):
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all()
    
class UserTypeView(viewsets.ModelViewSet):
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()
    
class VIPStatusView(viewsets.ModelViewSet):
    serializer_class = VIPStatusSerializer
    queryset = VIPStatus.objects.all()
    
class CustomUserView(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
