from django import forms
from .models import NewsPost

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Новость'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
        }
