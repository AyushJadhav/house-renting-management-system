from .models import Property, HouseImage
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Property
        fields=('title','address','price','bedroom','bathroom','availableFrom','furnished','lease','owner_email')
        
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = HouseImage
        fields = ['image']    