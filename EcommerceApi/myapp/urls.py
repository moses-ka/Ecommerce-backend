
from django.urls import path, include
from .views import index

urlpatterns = [
    path ('api/products', index.as_view() , name='api-products'),
    path ('api/product/<int:pk>', index.as_view() , name='api-products-update'),
]