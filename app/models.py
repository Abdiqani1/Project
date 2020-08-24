from django.db import models

# Create your models here.

class signup(models.Model):
    F_Name = models.CharField(max_length=50)
    E_mail =models.CharField(max_length=30)
    Username = models.CharField(max_length=20,unique=True)
    Password = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)
    Address = models.TextField(max_length=100)
    
    def __str__(self):
        return self.F_Name

        