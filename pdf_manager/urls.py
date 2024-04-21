# urls.py
from django.urls import path
from . import views

app_name = 'pdf_manager'
urlpatterns = [
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('pdf_list', views.pdf_list, name='pdf_list'),
    path('download/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
]