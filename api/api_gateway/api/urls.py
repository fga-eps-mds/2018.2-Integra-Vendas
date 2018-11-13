from django.urls import path
from django.conf.urls import url
from . import product_view
from . import notifications_view
from . import order_view
from . import view

urlpatterns = [
    #products urls
    path('api/create_product/', product_view.create_product),
    path('api/all_products/', product_view.all_products),
    path('api/delete_product/', product_view.delete_product),
    path('api/my_products_screen/', product_view.my_products_screen),
    path('api/get_product/', product_view.get_product),
    path('api/edit_product/', product_view.edit_product),

    #Notifications urls
    path('api/save_user_token/', notifications_view.save_user_token),
    path('api/send_push_message/', notifications_view.send_push_message),

    #Order urls
    path('api/create_order/', order_view.create_order),
    path('api/set_order_status/', order_view.set_order_status),
    path('api/buyer_orders/', order_view.buyer_orders),

    #Outras urls
    path('api/get_name/', view.get_name),
    path('api/orders_screen/', view.orders_screen),

    
]
