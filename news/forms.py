from news.models import News
from django import forms

class PostAddForm(forms.ModelForm):
    """ класс для создания форм """

    
    class Meta:
        model = News
        fields = ['title', 'about_what', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок новости'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полный текст новости',
                'rows': 10,
            }),
            'about_what':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'О чем ваша новость'
            })
        }
        