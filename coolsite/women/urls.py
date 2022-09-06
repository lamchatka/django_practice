from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/, name='home' -  указывает имя маршрута
    path('cats/<int:catid>/', categories, name='categories'),  # http://127.0.0.1:8000/cats/1/
    path('about/', about, name='about'),
    # http://127.0.0.1:8000/archive/2012/
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
    # r – это сырые строки (необработанные строки). Нужны для того, чтобы слеш \ не вызывал экранирование символов.
]
