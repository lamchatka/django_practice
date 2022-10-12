from django import forms
from .models import *


# то, что должно оторбразиться как поля  формы, названия должны быть такими же, как и в моделе
class AddWomenForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Содержимое")
    is_published = forms.BooleanField(label='Публикация',  required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории')
