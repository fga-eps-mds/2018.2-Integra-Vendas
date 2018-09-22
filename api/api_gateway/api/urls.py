from django.urls import path
from django.conf.urls import url
from api import views
from .views import delete_product

urlpatterns = [
    path('api/delete_product', delete_product),
]
