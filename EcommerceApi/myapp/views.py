from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class ProductManagment(APIView):
    permission_classes = [IsAuthenticated]
    
   
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        try:
            if serializer.is_valid():
                img_file = request.FILES.get('img')
                if img_file:
                    serializer.save(img=img_file)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return Response({'error': 'An error occurred while processing the request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        to_update = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        to_delete = get_object_or_404(Product, id=id)
        to_delete.delete()
        return Response({'deleted': True})
class getProducts(APIView):
    def get(self, request, *args, **kwargs):#this func return all the products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) 
        return Response(serializer.data)
class getProduct(APIView):
    def get(self, request, *args, **kwargs): #this func return one product
        id = kwargs.get('pk')
        product = get_object_or_404(Product, id=id)     
        serializer = ProductSerializer(product)
        return Response(serializer.data)
