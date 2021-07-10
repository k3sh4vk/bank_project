from django.core.validators import RegexValidator
from django.db import models
# Create your models here.


class RegisterDetails(models.Model):
    Name = models.CharField(max_length=30, null=False)                          # CANNOT BE NULL
    Mob_No = models.IntegerField(validators=[RegexValidator(r'^\d{0,9}')])      # MUST BE A NUMBER
    Aadhar_No = models.IntegerField(unique=True)                                # MUST BE UNIQUE
    Pan_No = models.CharField(max_length=20, unique=True)                       # MUST BE UNIQUE
    Current_Address = models.CharField(max_length=50)
    Permanent_Address = models.CharField(max_length=50)
    User_Type = models.CharField(max_length=10)
    Email = models.EmailField(max_length=30, unique=True)                       # MUST BE UNIQUE
    UserName = models.CharField(max_length=30, unique=True, null=False)         # MUST BE UNIQUE AND NOT NULL
    Password = models.CharField(max_length=15, null=False)                      # MUST BE NOT NULL