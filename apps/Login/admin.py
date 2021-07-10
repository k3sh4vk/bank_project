from django.contrib import admin
from apps.RegisterAccount.models import RegisterDetails
# Register your models here.


class RegisterRecords(admin.ModelAdmin):
    list_display = ['Name', 'Mob_No', 'Aadhar_No', 'Pan_No', 'Current_Address', 'Permanent_Address', 'User_Type', 'Email', 'UserName', 'Password']

admin.site.register(RegisterDetails, RegisterRecords)
