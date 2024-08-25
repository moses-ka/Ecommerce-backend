from sqlite3 import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product , User, Orders
from .serializers import ProductSerializer ,UserSerializer,CheckoutSerializer,OrderedProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import status

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
    
class searchProduct(APIView):
    def get(self, request, *args, **kwargs): #this func return all products with a specific tag
        search = kwargs.get('search')
        products = Product.objects.filter(title__icontains=search)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Hash the password before saving the user
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.save(password=hashed_password)

        # Create a token for the user
        user = serializer.instance
        Token.objects.create(user=user)


class SignInView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username,email=email, password=password)
        if user:
            return Response({ 'user_name': user.email ,'token': user.auth_token.key })
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)
class CheckoutView(generics.CreateAPIView):
    serializer_class = CheckoutSerializer
    
    def post(self, request, *args, **kwargs):
       print("Request data:", request.data)
       serializer = self.get_serializer(data=request.data)
       if serializer.is_valid():
           print("Serializer is valid")
           user = User.objects.get(email=serializer.validated_data['username'])
           total = serializer.validated_data['total']
           ordered_product_ids = serializer.validated_data['products']
           order = Orders.objects.create(user=user, total=total)
           print("Order created:", order)
           for product_id in serializer.validated_data['products']:
              try:
                  product = Product.objects.get(id=product_id)
                  order.products.add(product)
              except Product.DoesNotExist:
                  return Response({'error': f'Product with ID {product_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
           return Response({'message': 'Order placed successfully', 'total': total}, status=status.HTTP_201_CREATED)
       else:
           print("Serializer is not valid")
           print("Errors:", serializer.errors)
           return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
   
    

 
    def get(self, request, *args, **kwargs):
        username = request.data.get('username')
        
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        ordered_products = Orders.objects.filter(user=user)
        print(f"Orders for user {username}: {ordered_products}")
      # This will show the raw SQL query
        
        ordered_products_data = OrderedProductSerializer(ordered_products, many=True).data
        
        return Response({'ordered_products': ordered_products_data}, status=status.HTTP_200_OK)
