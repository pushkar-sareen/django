from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Customer

# Create your views here.

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email  = request.POST.get("password")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        customer =Customer.objects.create(user=user, Name=username, Email=email)
        customer.save()
        return redirect("login")    
    return render(request, "signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "login.html")

@login_required
def index(request):
    return render(request, "index.html", {'user':request.user})

def logout_user(request):
    logout(request)
    return redirect("login")
