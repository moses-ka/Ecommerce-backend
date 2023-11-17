from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    sex = models.CharField(max_length=120)
    img = models.ImageField(blank=True, null=True)
    size = models.CharField(max_length=120)
    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=120)
    def __str__(self):
        return self.username