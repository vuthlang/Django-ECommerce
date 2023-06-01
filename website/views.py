from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from website.models import Product


def index(request):
    # Récupérer tous les produits de la base de données
    products = Product.objects.all()

    # Passer les produits au template pour les afficher
    return render(request, 'index.html', {'products': products})


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'index_detail.html', {'product': product})


def related_products(request):
    products = Product.objects.order_by('?')
    context = {'products': products}
    return render(request, 'related_products.html', context)


def cart(request):
    return render(request, 'cart.html')


def signup(request):
 
    if request.user.is_authenticated:
        return redirect('/shop')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/shop')
         
        else:
            return render(request,'signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
 
 
def signin(request):
    if request.user.is_authenticated:
        return redirect('/shop')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/shop')
        else:
            form = AuthenticationForm()
            return render(request,'signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})
 
 
def signout(request):
    logout(request)
    return redirect('/shop/')
