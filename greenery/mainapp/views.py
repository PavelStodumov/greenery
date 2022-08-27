from itertools import product
from urllib import response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Greenery


def main(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context=context)

def products(request):
    product_list = Greenery.objects.all()
    context = {
        'title': 'Продукты',
        'product_list': product_list,
    }
    return render(request, 'mainapp/products.html', context)

def product(request, pk):
    product = get_object_or_404(Greenery, pk=pk)
    context = {
        'title': product.title,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)


def recepts(request):
    context = {
        'title': 'Рецепты',
    }
    return render(request, 'mainapp/recepts.html', context)