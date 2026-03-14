from django.shortcuts import render
from .models import ChaiVarity

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})
