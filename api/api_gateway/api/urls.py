from django.urls import path
from django.conf.urls import url
from api import views
from .views import delete_product, create_order, orders_screen

urlpatterns = [
    path('api/delete_product', delete_product),
    path('api/create_order', create_order),
    path('api/orders_screen', orders_screen),
]
