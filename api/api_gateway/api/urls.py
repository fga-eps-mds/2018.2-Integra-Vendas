from django.urls import path
from django.conf.urls import url
from api import views
from .views import delete_product, create_product, list_user_products

urlpatterns = [
    path('api/delete_product', delete_product),
    path('api/create_product/', create_product),
    path('api/list_user_products', list_user_products),
]
