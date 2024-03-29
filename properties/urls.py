from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'properties'
urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('lender', views.lender, name='lender'),
    path('', views.index, name='index'),
    path('property_details/<int:property_id>', views.property_details, name='property_details'),
]