from django.shortcuts import redirect, render
from users.models import Users
from .forms import UsersForm

# Create your views here.
def registration(request):
    return render(request,'Registration.html')
 
def login(request):
    return render(request,'login.html')
    
def submitRegistration(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successRegistration.html')  # Redirect to a success page after saving the user
    else:
        form = UsersForm()
    return render(request, 'Registration.html', {'form': form})
    
    
    