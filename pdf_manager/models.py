# models.py
from django.db import models

class PDFFile(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdf_files/')

    def __str__(self):
        return self.title
