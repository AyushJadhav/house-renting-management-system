# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PDFFile
from .forms import PDFFileForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_manager:pdf_list')
    else:
        form = PDFFileForm()
    return render(request, 'upload_pdf.html', {'form': form})

def pdf_list(request):
    pdfs = PDFFile.objects.all()
    return render(request, 'pdf_list.html', {'pdfs': pdfs})

def download_pdf(request, pdf_id):
    pdf = PDFFile.objects.get(pk=pdf_id)
    response = HttpResponse(pdf.pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf.pdf_file.name}"'
    return response
