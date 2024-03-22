from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'property_listing'
urlpatterns = [
    path('create', views.post_create, name='create'),
    path('post', views.post_house, name='post'),
    path('', views.index, name='index'),
   
]