from django import forms
from django.core.exceptions import ValidationError

from .models import *


# то, что должно оторбразиться как поля  формы, названия должны быть такими же, как и в моделе
class AddWomenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # конструктор класса
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Women  # связь с моделью
        fields = ['title', 'slug', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 68, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title
