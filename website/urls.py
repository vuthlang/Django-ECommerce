from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path('product/<int:product_id>/', views.product_view, name='product_view'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path("cart/", views.cart, name="cart"),
    path("login/", views.login, name="login"),
]
