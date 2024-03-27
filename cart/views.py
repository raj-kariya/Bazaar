from django.shortcuts import render, redirect
from .models import Cart
from Products.models import Product

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(item=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')


# def remove_to_cart(request, item_id):

