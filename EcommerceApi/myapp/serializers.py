from rest_framework import serializers
from .models import Product  # Product model is in the same directory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # This will include all fields in the serializer
        