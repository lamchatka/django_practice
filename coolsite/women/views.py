from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AddWomenForm


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
    if request.method == 'POST':  # создаем экземпляр класса
        form = AddWomenForm(request.POST)
        if form.is_valid():  # проверка на корректность данных
            print(form.cleaned_data)  # отобразим очищенные данные
    else:
        form = AddWomenForm()
    context = {
        'title': 'Добавление страницы',
        'form':  form,
    }
    return render(request, 'women/add_page.html', context=context)


def contact(request):
    return HttpResponse('<h1> Контактная форма</h1>')


def login(request):
    return HttpResponse('<h1> Авторизация</h1>')


def show_post(request, post_slug):
    women = get_object_or_404(Women, slug=post_slug)
    context = {
        'women': women,
        'title': women.title,
        'cat_selected': women.cat_id
    }
    return render(request, 'women/read_post.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.get(slug=cat_slug)
    women_list = Women.objects.filter(cat_id=cat.id)
    if len(women_list) == 0:
        raise Http404()

    context = {
        'women_list': women_list,
        'cat_selected': cat.id,
        'title': 'Отображение по рубрикам'
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
