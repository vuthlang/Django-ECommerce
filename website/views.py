from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from website.models import CartItem, Product


def index(request):
    # Récupérer tous les produits de la base de données
    products = Product.objects.all()

    # Passer les produits au template pour les afficher
    return render(request, 'index.html', {'products': products})


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'index_detail.html', {'product': product})



def cart(request):
  return render(request, 'cart.html')


def add_to_cart(request, product_id):
    # Récupérer le produit à partir de son ID
    product = get_object_or_404(Product, id=product_id)

    # Vérifier si un panier existe déjà dans la session de l'utilisateur
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    # Vérifier si le produit est déjà dans le panier
    if product_id in cart:
        # Si oui, augmenter la quantité du produit dans le panier
        cart[product_id]['quantity'] += 1
    else:
        # Sinon, ajouter le produit au panier avec une quantité de 1
        cart[product_id] = {
            'quantity': 1,
            'product_name': product.product_name,
            'price': str(product.price)
        }

    # Enregistrer les modifications du panier dans la session
    request.session['cart'] = cart

    # Rediriger l'utilisateur vers la page cart.html après l'ajout du produit
    return redirect('cart')





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
