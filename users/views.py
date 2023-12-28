from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
# function based view
def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"form":form})