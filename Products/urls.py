from django.urls import path
# from django.contrib.auth import views as auth_views
# from . views import homepage
from .views import Home
urlpatterns = [
    path('', Home.as_view()),    
] 
# print(type(homepage))