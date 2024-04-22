from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, RentCalculationForm
from django.http import HttpResponse
from django.urls import reverse
from rentCalculationsUtility.rentCalculations.rentCalculations import RentCalculator
# Create your views here.
def registration(request):
    if request.method == "POST":
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        countryCode = request.POST['country_code']
        phone = request.POST['phone']
        userType = request.POST.get('user_type') 
        if userType == 'lender':
            isLender = True
        else:
            isLender = False
        
        # Check if username already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'Registration.html', {'error': 'Username already exists'})
    
        user = User.objects.create_user(first_name=fname, last_name=lname, email=email, password=password, username=email)
        Signup.objects.create(user=user, phone=phone, isLender=isLender)
        
        #user = User.objects.create(firstName=fname, lastName=lname, email=email, password=password, phone=countryCode+phone, isLender=isLender)
        
        messages.success(request, "Register Successful")
        return render(request,'register_done.html')
    return render(request, 'Registration.html', locals())
 
def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(username=email, password=pwd)
        print(user)
        if user:
            #user_details = Signup.objects.filter(user=user.email)
            userd = get_object_or_404(Signup, user=user)
            if userd.isLender:
                login(request, user)
                messages.success(request, "Lender User")
                return redirect(reverse('properties:lender'))
            else:
                login(request, user)
                messages.success(request, "Renter User")
                return redirect(reverse('properties:index'))
        else:
            messages.error(request, "Invalid User")
            return redirect('login_user')
           
    return render(request, 'login.html', locals())
    
@login_required
def edit(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('properties:index'))
    else:
        user_form=UserEditForm(instance=request.user)
    return render(request,'edit.html',{'user_form':user_form})    
    
   
@login_required
def profile(request):
    try:
        print(request.user)
        userInfo = Signup.objects.get(user=request.user)
    except Signup.DoesNotExist:
        # Handle the case where the object does not exist
        # For example, you can return a 404 response
        return HttpResponse("Signup not found")
    
    print(userInfo)
    return render(request, 'userInfo.html', {'userInfo': userInfo})        
    
def rent_calculation(request):
    if request.method == 'POST':
        form = RentCalculationForm(request.POST)
        if form.is_valid():
            first_month_rent = form.cleaned_data['first_month_rent']
            subsequent_month_rent = form.cleaned_data['subsequent_month_rent']
            num_of_months = form.cleaned_data['num_of_months']
            rent_calculator = RentCalculator(first_month_rent, subsequent_month_rent, num_of_months)
            total_rent = rent_calculator.calculate_rent()  # Calculate total rent
            print("Total rent:", total_rent)
            return render(request, 'result.html', {'total_rent': total_rent})
    else:
        form = RentCalculationForm()
    return render(request, 'rent_calculation.html', {'form': form})    