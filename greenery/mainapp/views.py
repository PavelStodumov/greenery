from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

MAIN_MENU = [
    {'title': 'Продукты', 'url': 'products'},
    {'title': 'Рецепты', 'url': 'recepts'}
]

def main(request):
    context = {
        'menu': MAIN_MENU,
    }
    return render(request, 'mainapp/index.html', context=context)

def products(request):
    return HttpResponse('Products')

def recepts(request):
    return HttpResponse('Recepts')