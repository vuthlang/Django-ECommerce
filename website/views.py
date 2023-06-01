# from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
# return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import get_object_or_404, render

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


def login(request):
    return render(request, 'login.html')
