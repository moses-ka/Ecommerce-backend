
from django.urls import path, include
from .views import getProducts , ProductManagment ,getProduct,SignInView,SignUpView,searchProduct,CheckoutView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path ('api/products', getProducts.as_view() , name='all-products'),
    path ('api/product/<int:pk>', getProduct.as_view() , name='api-product'),
   path('api/products/search/<str:search>', searchProduct.as_view() , name='api-products-search'),
    path ('api/product-update/<int:pk>', ProductManagment.as_view() , name='api-products-update'),
    path ('api/product-delete/<int:pk>', ProductManagment.as_view() , name='api-products-delete'),
    path ('api/product-add', ProductManagment.as_view() , name='api-products-add'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('products/checkout', CheckoutView.as_view() , name='api-products-checkout'),
    path ("ordered-products", CheckoutView.as_view() , name='api-ordered-products'),
]