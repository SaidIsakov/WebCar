from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    """ Форма для аутентификации пользователя"""
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class':'form-control',
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
        })
    )
    
class RegistrationForm(UserCreationForm):
    """ Регимтрация пользователя """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Имя Пользователя'
        })
        )
    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Электронная почта',
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Пароль'
        })
        )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Подтвердите пароль'
        })
        )