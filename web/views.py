from django.shortcuts import render
from web.models import newsflash

# Create your views here.

def index (request):
    flashnews = newsflash.objects.all()
    context = {
        "flashnews" : flashnews
    }
    return render(request, 'pages/index.html', context=context)

def about (request):
    return render(request, 'pages/about.html')

def contact (request):
    return render(request, 'pages/contact.html')

def com_course (request):
    return render(request, 'pages/com-courses.html')

def dis_course (request):
    return render(request, 'pages/dis-courses.html')