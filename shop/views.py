from django.shortcuts import render
from .models import *

# Create your views here.

def customerpage(request):
    return render(request,'customer.html')

def prodectdetailpage(request):
    proresults = Product.objects.all()
    return render(request,'productdetail.html',{'proresults':proresults})
