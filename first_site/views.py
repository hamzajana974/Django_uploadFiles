from django.http import HttpResponse
from django.shortcuts import render
from .models import FilesUpload

def home(request):
    if request.method == "POST":
        files2 = request.FILES['files1']
        document = FilesUpload.objects.create(files1=files2)
        document.save()
        return HttpResponse('Hello World!')
    return render(request,"home.html")

def result(request):
    return HttpResponse('Han Bhai')