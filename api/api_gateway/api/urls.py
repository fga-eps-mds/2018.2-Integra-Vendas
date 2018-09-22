from django.urls import path
from django.conf.urls import url
from api import views
from .views import ProductDelete

urlpatterns = [
    path('api/product_delete', ProductDelete),
]
