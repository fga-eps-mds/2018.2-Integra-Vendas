from django.urls import path
from django.conf.urls import url
from api import views
from .views import delete_product, create_order

urlpatterns = [
    path('api/delete_product', delete_product),
    path('api/create_order', create_order),
]
