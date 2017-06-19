from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm


def upload(request):
    documents = Document.objects.all()
    return render(request, 'document/upload.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'document/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'document/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_name = request.user
            obj.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'document/model_form_upload.html', {
        'form': form
    })
