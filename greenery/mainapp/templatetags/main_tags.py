from django import template


register = template.Library()

@register.inclusion_tag('mainapp/main_menu.html')
def main_menu():
    MAIN_MENU = [
        {'title': 'Продукты', 'url': 'products'},
        {'title': 'Рецепты', 'url': 'recepts'},
        {'title': 'На главную', 'url': 'main'},
    ]
    return({'menu_list': MAIN_MENU})