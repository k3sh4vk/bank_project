from django.core.validators import RegexValidator
from django.db import models
# Create your models here.


class RegisterDetails(models.Model):
    Name = models.CharField(max_length=30, null=False)
    Mob_No = models.IntegerField(validators=[RegexValidator(r'^\d{0,9}')])
    Aadhar_No = models.IntegerField(unique=True)
    Pan_No = models.CharField(max_length=20, unique=True)
    Current_Address = models.CharField(max_length=50)
    Permanent_Address = models.CharField(max_length=50)
    User_Type = models.CharField(max_length=10)
    Email = models.EmailField(max_length=30, unique=True)
    UserName = models.CharField(max_length=30, unique=True, null=False)
    Password = models.CharField(max_length=15, null=False)