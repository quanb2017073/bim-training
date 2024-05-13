from django.contrib import admin
from .models import UserRole, UserType, UserProfile, CustomUser, VIPStatus
# Register your models here.

class userroleAdmin(admin.ModelAdmin):
    list_display = ('role_name',)
admin.site.register(UserRole, userroleAdmin)

class usertypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
admin.site.register(UserType, usertypeAdmin)

class vipstatusAdmin(admin.ModelAdmin):
    list_display = ('VIP_status_name',)
admin.site.register(VIPStatus, vipstatusAdmin)

class userprofileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]
admin.site.register(UserProfile, userprofileAdmin)

class customuserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]
admin.site.register(CustomUser, customuserAdmin)
