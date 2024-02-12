from rest_framework import serializers
from .models import Product  # Product model is in the same directory
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