from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product 
from django.contrib.auth.models import User


class ProductsApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_all_products(self) :
        response = self.client.get('http://127.0.0.1:8000/api/products')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    # def test_get_one_product(self) :
   
    #     headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Origin': 'same-origin'}
    #     response = self.client.get('http://127.0.0.1:8000/api/product/17',headers=headers)
    #     print(response ,'this is response')
    #     print(response.content ,'this is response content')
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
