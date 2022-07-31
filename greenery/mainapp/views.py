from itertools import product
from urllib import response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Greenery

MAIN_MENU = [
    {'title': 'Продукты', 'url': 'products'},
    {'title': 'Рецепты', 'url': 'recepts'},
    {'title': 'На главную', 'url': 'main'},
]

def main(request):
    context = {
        'title': 'Главная',
        'menu': MAIN_MENU,
    }
    return render(request, 'mainapp/index.html', context=context)

def products(request):
    product_list = Greenery.objects.all()
    context = {
        'title': 'Продукты',
        'menu': MAIN_MENU,
        'product_list': product_list,
    }
    return render(request, 'mainapp/products.html', context)

def product(request, pk):
    product = get_object_or_404(Greenery, pk=pk)
    context = {
        'title': product.title,
        'menu': MAIN_MENU,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)


def recepts(request):
    context = {
        'title': 'Рецепты',
        'menu': MAIN_MENU,
    }
    return render(request, 'mainapp/recepts.html', context)