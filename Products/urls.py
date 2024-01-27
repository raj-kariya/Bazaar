from django.urls import path
# from django.contrib.auth import views as auth_views
# from . views import homepage
from .views import Home
from . import views
urlpatterns = [
    path('', Home.as_view()),  
    path('<slug:product_slug>/', views.product_all, name='product_all'),
    path('<slug:category_slug>/', views.category_list, name='category_list'),
    # path('<slug:slug>', views.product_detail, name='product_detail'),  
] 
# print(type(homepage))