from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('registration/', views.registration, name='registration'), 
    #path('submitRegistration/', views.submitRegistration, name='submitRegistration'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/',views.edit, name='profile'),
    path('change_password/', auth_view.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
    path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='password_change_done'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]