from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    isLender = models.BooleanField()
    
    def __str__(self):
        return self.firstName+" "+self.lastName
        
class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=13)
    isLender = models.BooleanField()
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name        