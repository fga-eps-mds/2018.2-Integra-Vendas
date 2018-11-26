from django.urls import path
from django.conf.urls import url
from . import product_views
from . import notifications_views
from . import order_views
from . import views

urlpatterns = [
    #products urls
    path('api/create_product/', product_views.create_product),
    path('api/all_products/', product_views.all_products),
    path('api/delete_product/', product_views.delete_product),
    path('api/my_products_screen/', product_views.my_products_screen),
    path('api/get_product/', product_views.get_product),
    path('api/edit_product/', product_views.edit_product),

    #Notifications urls
    path('api/save_user_token/', notifications_views.save_user_token),
    path('api/send_push_message/', notifications_views.send_push_message),

    #Order urls
    path('api/create_order/', order_views.create_order),
    path('api/set_order_status/', order_views.set_order_status),
    path('api/buyer_orders/', order_views.buyer_orders),

    #Outras urls
    path('api/get_name/', views.get_name),
    path('api/orders_screen/', views.orders_screen),

    
]
