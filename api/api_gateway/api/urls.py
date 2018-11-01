from django.urls import path
from django.conf.urls import url
from api import views
from .views import (create_product, delete_product, create_order, orders_screen,
                    all_products, my_products_screen, get_product, get_name,
                    edit_product, buyer_orders, set_order_status, save_user_token, send_push_message)

urlpatterns = [
    path('api/create_product/', create_product),
    path('api/all_products/', all_products),
    path('api/delete_product/', delete_product),
    path('api/create_order/', create_order),
    path('api/orders_screen/', orders_screen),
    path('api/my_products_screen/', my_products_screen),
    path('api/get_product/', get_product),
    path('api/get_name/', get_name),
    path('api/set_order_status/', set_order_status),
    path('api/edit_product/', edit_product),
    path('api/buyer_orders/', buyer_orders),
    path('api/save_user_token/', save_user_token),
    path('api/send_push_message/', send_push_message),
]
