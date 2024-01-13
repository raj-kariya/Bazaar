# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from Products.models import Product
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