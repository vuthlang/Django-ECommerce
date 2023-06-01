from django.urls import path
from .views import signin, signout, signup

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path('product/<int:product_id>/', views.product_view, name='product_view'),
    #path('cart/', views.add_to_cart, name='add_to_cart'),
    path("cart/", views.cart, name="cart"),

    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('signin/', views.signin, name = 'login'),
    path('signout/', views.signout, name = 'logout'),
    path('signup/', views.signup, name ='signup'),
]
