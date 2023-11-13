
from django.urls import path, include
from .views import getProducts , ProductManagment ,getProduct
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path ('api/products', getProducts.as_view() , name='all-products'),
    path ('api/product/<int:pk>', getProduct.as_view() , name='api-product'),
    path ('api/product-update/<int:pk>', ProductManagment.as_view() , name='api-products-update'),
    path ('api/product-delete/<int:pk>', ProductManagment.as_view() , name='api-products-delete'),
    path ('api/product-add', ProductManagment.as_view() , name='api-products-add'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    
]