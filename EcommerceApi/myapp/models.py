from django.db import models

# Create your models here.

class Product(models.Model):
    sex_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    ]
    color_choices = [
        ('Black', 'Black'),
        ('White', 'White'),
    ]
    size_choices = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
        
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    sex = models.CharField(max_length=1, choices=sex_choices,null=True, blank=True)
    img = models.ImageField(blank=True, null=True)
    size = models.CharField(max_length=2 ,choices=size_choices ,null=True, blank=True)
    tags = models.CharField(max_length=120,null=True, blank=True)
    color = models.CharField(max_length=120, choices=color_choices ,null=True, blank=True)
    
    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=120)
    def __str__(self):
        return self.username

from django.contrib.auth.models import User
from django.db import models
from django.contrib import auth

class OrderedProduct(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=auth.get_user)
    total_price = models.DecimalField(decimal_places=4, max_digits=10000)

    def __str__(self):
        return ', '.join([product.title for product in self.products.all()])