from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm



from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from website.models import CartItem, Product








def index(request):
    

    products = Product.objects.all()


    return render(request, 'index.html', {'products': products})

def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'index_detail.html', {'product': product})


def related_products(request):
    products = Product.objects.order_by('?')
    context = {'products': products}
    return render(request, 'related_products.html', context)



def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_price = item['quantity'] * product.price
        cart_items.append({
            'product_id': product_id,
            'product_name': product.product_name,
            'price': product.price,
            'quantity': item['quantity'],
            'total_price': total_price
        })

    context = {
        'cart_items': cart_items
    }

    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']


    if product_id in cart:
    
        cart[product_id]['quantity'] += 1
    else:
       
        cart[product_id] = {
            'quantity': 1,
            'product_name': product.product_name,
            'price': str(product.price)
        }

    
    request.session['cart'] = cart

    return redirect('cart')





def remove_from_cart(request, product_id):
   
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]
       
        request.session['cart'] = cart
    return redirect('cart')

def update_quantity(request, product_id):
   
    cart = request.session.get('cart', {})
  
    if product_id in cart:
        
        quantity = request.GET.get('quantity', 1)
        cart[product_id]['quantity'] = int(quantity)
     
        request.session['cart'] = cart
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
