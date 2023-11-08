from django.shortcuts import render
from django.http import HttpResponse

from .models import productlisting

def home(request):
    products_data=productlisting.objects.all()
    print(products_data)
    return render(request,'productListing.html',{'products':products_data})
def pd(request):
    return render(request,'productdetails.html')
def cart(request):
    return render(request,'viewcart.html')
def login(request):
    return render(request,'login.html')