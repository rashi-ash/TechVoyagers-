from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product, Cart


@login_required(login_url='/login/')

def home(request):
    products_data=Product.objects.all()
    print(products_data)
    return render(request,'productListing.html',{'products':products_data})

def pd(request, id):
    context = {'object': Product.objects.get(id=id)}
    return render(request,'productdetails.html', context)

def add_cart(request,id):
    ob = Product.objects.get(id=id)
    Cart.objects.get(user=request.user).product.add(ob)
    return redirect('cart')
@login_required
def cart(request):
    user_cart,created=Cart.objects.get_or_create(user=request.user)
    return render(request,'viewcart.html', {
        'cart': user_cart
    })


def login(request):
    form=UserCreationForm()
    if request.method=='POST':
        if 'login' in request.POST:
            print('login')
            username1 = request.POST.get('user-email')
            password = request.POST.get('password')
         
            user = authenticate(request,username=username1,password=password)
            if user is not None:
                auth_login(request,user)     
                return redirect('home')
            
        else:
            print(request.POST)
            print('register')
            form=UserCreationForm(request.POST)
            if form.is_valid():
                print('its Valid')
                form.save()
    return render(request,'login.html',{
        'form':form
    })
def logoutview(request):
    logout(request)
    return redirect('login')