from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'properties'
urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('lender', views.lender, name='lender'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('send_email/<int:property_id>/<str:owner_email>/', views.send_email, name='send_email'),
    path('property_details/<int:property_id>', views.property_details, name='property_details'),
    path('success', views.email_success_page, name='email_success_page'),
    path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('mark-as-booked/<int:property_id>/', views.mark_property_as_booked, name='mark_property_as_booked'),
    path('mark-as-available/<int:property_id>/', views.mark_property_as_available, name='mark_property_as_available'),
]