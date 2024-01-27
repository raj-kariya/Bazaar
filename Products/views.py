# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from Products.models import Product,Category
from django.shortcuts import get_object_or_404,render
from django.db import connection
# from django.shortcuts import render
# from users.forms import User
# def homepage(request):
#     products = Product.objects.all()
#     context = {'products' : products}
#     if not request.user:
#         raise PermissionError
#     return render(request,"Products/index.html")

class Home(ListView):
    model = Product
    template_name = 'Products/index.html'

def product_all(request,product_slug):
    products = Product.objects.filter(slug = product_slug)
    # print(products.entry_set.all().values())
    # print(connection.queries[-1])
    return render(request, 'Products/category.html', {'products': products})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'Products/category.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'Products/index.html', {'product': product})