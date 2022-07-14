from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('products/', products, name='products'),
    path('recepts/', recepts, name='recepts'),
]
