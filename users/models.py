from django.db import models

# Create your models here.
class Users(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    isLender = models.BooleanField()
    
def __str__(self):
    return self.firstNmae+" "+self.lastName