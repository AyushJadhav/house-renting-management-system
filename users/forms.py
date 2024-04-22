from django import forms
from .models import Signup
from django.contrib.auth.models import User

# class UsersForm(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = ['firstName', 'lastName', 'email', 'phone', 'isLender']
        
class UserEditForm(forms.ModelForm):
    phone = forms.CharField(max_length=13)
    class Meta:
        model=User
        fields=('first_name','last_name','email',)
        
class RentCalculationForm(forms.Form):
    first_month_rent = forms.DecimalField(label='First Month Rent')
    subsequent_month_rent = forms.DecimalField(label='Subsequent Month Rent')
    num_of_months = forms.IntegerField(label='Number of Months')
    
             