from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *




def index(request):  # ссылка на класс HttpRequest(куки, сессии и тд, get/post запросы)
    # return HttpResponse("Страница приложения women.")  # экземпляр класса
    women_list = Women.objects.all()
    context = {
        'women_list': women_list,
        'title': 'Главная страница',
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def add_page(request):
    return HttpResponse('<h1> Добавление страницы</h1>')


def contact(request):
    return HttpResponse('<h1> Контактная форма</h1>')


def login(request):
    return HttpResponse('<h1> Авторизация</h1>')


def show_post(request, post_id):
    women = Women.objects.get(pk=post_id)
    context = {
        'women': women
    }
    return render(request, 'women/read_post.html', context=context)


def show_category(request, cat_id):
    women_list = Women.objects.filter(cat_id=cat_id)

    if len(women_list) == 0:
        raise Http404()

    context = {
        'women_list': women_list,
        'cat_selected': cat_id,
        'title': 'Отображение по рубрикам'
    }

    return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
