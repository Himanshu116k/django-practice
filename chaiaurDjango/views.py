from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')
   # return HttpResponse("Hello World")

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')