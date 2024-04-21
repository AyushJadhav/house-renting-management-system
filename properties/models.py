from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
# Create your models here.
class Property(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #image=models.ImageField(upload_to='images/%y/%m/%d')
    address=models.TextField(blank=True)
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    bedroom=models.IntegerField()
    bathroom=models.IntegerField()
    availableFrom=models.DateField()
    furnished=models.BooleanField(default=False)
    lease=models.CharField(max_length=200)
    created=models.DateField(auto_now_add=True)
    owner_email = models.EmailField(blank=False, null=False)
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

class HouseImage(models.Model):
    house = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='house_images/', blank=True, null=True)   