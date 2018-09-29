from django.urls import path
from django.conf.urls import url
from api import views
from .views import create_product, delete_product, create_order, orders_screen, all_products

urlpatterns = [
    path('api/create_product/', create_product),
    path('api/all_products/', all_products),
    path('api/delete_product/', delete_product),
    path('api/create_order/', create_order),
    path('api/orders_screen/', orders_screen),
]
