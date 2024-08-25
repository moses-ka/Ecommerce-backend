from rest_framework import serializers
from .models import Product,Orders
from django.contrib.auth.models import User

from rest_framework.validators import UniqueValidator
class ProductSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = '__all__'  # This will include all fields in the serializer
        


class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ['username','email', 'password' ]
        extra_kwargs = {'password': {'write_only': True}}


class CheckoutSerializer(serializers.Serializer):
    username = serializers.CharField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    products = serializers.ListField(child=serializers.IntegerField())  # List of product IDs




class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'