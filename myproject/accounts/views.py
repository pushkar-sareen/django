from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Customer, Product, Order

# Create your views here.

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email  = request.POST.get("email")

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


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")

        product = Product.objects.create(name=name, price=price)
        product.save()
        return redirect("/")
    return render(request, "add-product.html") 

def get_product(request):
    products = Product.objects.all()
    return render(request, "product.html", {'products':products})


def add_order(request, product_id):
    customer = Customer.objects.get(user= request.user)
    product = Product.objects.get(id=product_id)
    order = Order.objects.create(
        customer = customer
    )
    order.product.add(product)
    order.save()
    return redirect("order")

def get_order(request):
    orders = Order.objects.filter(customer__user=request.user)
    return render(request, "order.html", {"orders": orders})