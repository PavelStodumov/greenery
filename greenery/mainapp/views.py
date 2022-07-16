from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

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
    context = {
        'title': 'Продукты',
        'menu': MAIN_MENU,
    }
    return render(request, 'mainapp/products.html', context)

def recepts(request):
    return HttpResponse('Recepts')