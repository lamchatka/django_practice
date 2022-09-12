from django import template
from women.models import *

register = template.Library()  # экземпляр класса Library в модуле template


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)  # возваращает коллекцию данных


@register.inclusion_tag("women/list_categories.html")
def show_categories(sort=None, cat_selected=0):  # sort хранит значение полей, по которому будет проводиться сортировка
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats,
            "cat_selected": cat_selected}  # возращает словарь, который будет передаваться шаблону, возвращает фрагмент html страницы


@register.inclusion_tag("women/menu_list.html")
def show_menu():
    menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
    ]
    return {'menu': menu}
