from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', 'email', 'phone', 'isLender']
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=('firstName','lastName','email','phone')
        
             