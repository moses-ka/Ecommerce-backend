from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser , FormParser
from .models import Product
from .serializers import ProductSerializer
from django.conf import settings
# Create your views here.

class index(APIView):
    def get(self, request , *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    def post(self, request , *args, **kwargs):
      
        serializer = ProductSerializer(data=request.data)
        try:
            if serializer.is_valid():
                img_file = request.FILES.get('img')
                # Check if img_file exists before trying to save it
                if img_file:
                    # Save the image to the 'media/uploads/' directory
                    serializer.save(img=img_file)

                # Save the product details to the database
                serializer.save()

                # Return a success response
                return Response(serializer.data, status=201)

            # Return a response with validation errors
            return Response({'error': serializer.errors}, status=400)
        except Exception as e:
            # Log the exception for debugging
            print(f"An error occurred: {str(e)}")
            
            # Return a generic error response
            return Response({'error': 'An error occurred while processing the request'}, status=500)
    def put(self, request , *args, **kwargs):
        id = kwargs.get('pk')
        to_update = Product.objects.get(id=id)
        serializer = ProductSerializer(to_update, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def delete(self, request , *args, **kwargs):
        pass