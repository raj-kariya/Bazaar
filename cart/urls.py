# urls.py

from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    # ... your other URL patterns ...
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('view-cart/', views.view_cart, name='view_cart'),
]
