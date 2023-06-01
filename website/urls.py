from django.urls import path
from .views import signin, signout, signup

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path('product/<int:product_id>/', views.product_view, name='product_view'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path("cart/", views.cart, name="cart"),
    
    path('signin/', views.signin, name = 'login'),
    path('signout/', views.signout, name = 'logout'),
    path('signup/', views.signup, name ='signup'),
]
