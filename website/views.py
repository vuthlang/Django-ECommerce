# from django.shortcuts import render
import json
from django.http import HttpResponse

# def index(request):
# return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import get_object_or_404, render

from website.models import Product


# views.py

from django.shortcuts import render
from django.http import JsonResponse

def add_to_cart(request):
    if request.method == 'POST':
        # Retrieve the product ID and quantity from the request
        data = json.loads(request.body)
        product_id = data.get('productId')
        quantity = data.get('quantity')

        # Perform any necessary logic to add the product to the cart
        # For example, you can store the product ID and quantity in the session or a database

        # Return a JSON response indicating the success or failure of adding the product to the cart
        return JsonResponse({'message': 'Product added to cart!'})

    # Handle the case where the request method is not POST
    return JsonResponse({'message': 'Invalid request.'}, status=400)







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
