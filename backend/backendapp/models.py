from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRole(models.Model):
    role_name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self) -> str:
        return self.role_name

class UserType(models.Model):
    type_name = models.CharField(max_length=50, unique=True,null=True)
    
    def __str__(self) -> str:
        return self.type_name
    
class VIPStatus(models.Model):
    VIP_status_name = models.CharField(max_length=50, unique=True,null=True)
    
    def __str__(self) -> str:
        return self.VIP_status_name
    
class CustomUser(User):
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str: 
        return self.pk
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    is_company = models.BooleanField(default=False)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)
    vipStatus  = models.ForeignKey(VIPStatus, on_delete=models.CASCADE, null=True)
    

    



    

    