from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm, ImageForm, HouseForm
from .models import Property, HouseImage
from users.models import Signup
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import Context
from django.utils.html import strip_tags

# views.py
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def post_create(request):
    if request.method=='POST':
        signup = Signup.objects.get(user=request.user)
        is_lender = signup.isLender
        if is_lender:
            house_form=PostCreateForm(data=request.POST)
            image_forms = [ImageForm(request.POST, request.FILES, prefix=str(x)) for x in range(5)]
            if house_form.is_valid() and all([form.is_valid() for form in image_forms]):
                house = house_form.save(commit=False)
                house.user = request.user
                house.save()
                for form in image_forms:
                    if form.cleaned_data.get('image'):
                        HouseImage.objects.create(house=house, image=form.cleaned_data['image'])
                #return HttpResponse("Created")   
                return redirect(reverse('properties:property_details', kwargs={'property_id': house.id}))
    else:
        form =PostCreateForm(data=request.GET)
        image_forms = [ImageForm(prefix=str(x)) for x in range(5)]
        return render(request,'create.html',{'form':form, 'image_forms': image_forms})  



# def property(request):
#     prop = House.objects.all()
#     return render(request, 'property_list.html', {'houses': houses})


@login_required
def property_details(request, property_id):
    if hasattr(request.user, 'signup') and (request.user.signup.isLender or not request.user.signup.isLender):
        house = Property.objects.get(id=property_id)
        return render(request, 'house_detail.html', {'property': house})
    else:
        return HttpResponse('Login required!')

def lender(request):
    signup = Signup.objects.get(user=request.user)
    propertyObjs= Property.objects.filter(user=signup.user)
    print(signup)
    return render(request, 'Lender.html', {'properties':propertyObjs, 'logged_user':signup},)
    
def index(request):
    if request.method=='POST':
        current_user=request.user
        signup = Signup.objects.get(user=request.user)
        property_id=request.POST.get('property_id')
        propertyObj=get_object_or_404(Property,id=property_id)
    properties=Property.objects.all()
    images=HouseImage.objects.all()
    #logged_user=request.user
    return render(request,'index.html',{'properties':properties , 'images':images },)    
    
def property_delete(request, pk):
    house = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        house.delete()
        return redirect('house_list')
    return render(request, 'house_confirm_delete.html', {'house': house})
    
def house_update(request, pk):
    house = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        house_form = HouseForm(request.POST, instance=house)
        if house_form.is_valid():
            house_form.save()
            return render(request, 'house_detail.html', {'property': house})
    else:
        house_form = HouseForm(instance=house)
    return render(request, 'house_form.html', {'house_form': house_form})    
    
def services(request):
  return render(request, 'services.html')
  
def send_email(request,property_id, owner_email):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        property = get_object_or_404(Property, id=property_id)
        template = get_template('property_email.html')
        email_message = template.render({'property': property})
        text_content = strip_tags(email_message)
        print(text_content)
        msg = EmailMultiAlternatives(subject, message+text_content, email, [owner_email])
       
        msg.send()
        # Add your email sending logic here
        #send_mail(subject, message, 'jadhavayush13@gmail.com', [owner_email] )
        
        # Redirect after sending email
        return HttpResponseRedirect(reverse('properties:email_success_page'))  # Redirect to a success page

    # If method is not POST, render the form
    house = Property.objects.get(id=property_id)
    return render(request, 'house_detail.html', {'property': house})  
    

def email_success_page(request):
    return render(request, 'email_success_page.html')
    
def edit_property(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('property_details', property_id=property_id)
    else:
        form = PostCreateForm(instance=property_instance)

    return render(request, 'edit_property.html', {'form': form})    

def mark_property_as_booked(request, property_id):
    property = Property.objects.get(pk=property_id)
    property.is_booked = True
    property.save()
    return redirect('properties:lender')
    
def mark_property_as_available(request, property_id):
    property = Property.objects.get(pk=property_id)
    property.is_booked = False
    property.save()
    return redirect('properties:lender')    