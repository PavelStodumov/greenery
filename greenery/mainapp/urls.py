from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', product, name='product'),
    path('recepts/', recepts, name='recepts'),
]
