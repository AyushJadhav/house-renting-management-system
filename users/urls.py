from django.contrib import admin
from django.urls import path, include
from users import views
urlpatterns = [
    path('registration/', views.registration, name='registration'), 
    path('submitRegistration/', views.submitRegistration, name='submitRegistration'),
    path('login/', views.login, name='login'),
]