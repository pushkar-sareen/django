from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True) 


class Product(models.Model):
    name = models.CharField(max_length=50)
    price =models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)