from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm, ImageForm
from .models import Property, HouseImage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

# views.py
from django.shortcuts import render, redirect


# Create your views here.
@login_required
def post_create(request):
    if request.method=='POST':
        house_form=PostCreateForm(data=request.POST)
        image_forms = [ImageForm(request.POST, request.FILES, prefix=str(x)) for x in range(5)]
        if house_form.is_valid() and all([form.is_valid() for form in image_forms]):
            house = house_form.save()
            for form in image_forms:
                if form.cleaned_data.get('image'):
                    HouseImage.objects.create(house=house, image=form.cleaned_data['image'])
            return HttpResponse("Created!")
    else:
        form =PostCreateForm(data=request.GET)
        image_forms = [ImageForm(prefix=str(x)) for x in range(5)]
    return render(request,'create.html',{'form':form, 'image_forms': image_forms})  

def post_house(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save()
            
            return redirect('index')
    else:
        form = PostCreateForm()
    return render(request, 'create.html', {'form': form})

def house_list(request):
    houses = House.objects.all()
    return render(request, 'house_list.html', {'houses': houses})



def house_detail(request, house_id):
    house = Property.objects.get(id=house_id)
    return render(request, 'house_detail.html', {'house': house})
    
def index(request):
    if request.method=='POST':
        property_id=request.POST.get('property_id')
        propertyObj=get_object_or_404(Property,id=property_id)
    properties=Property.objects.all()
    images=HouseImage.objects.all()
    #logged_user=request.user
    return render(request,'index.html',{'properties':properties , 'images':images},)    