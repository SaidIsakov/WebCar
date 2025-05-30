from django.shortcuts import render,redirect
from .models import Category,Cars
from django import forms
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import login,logout
from django.contrib import messages




def index(request):
    
    category = Category.objects.all()
    post = Cars.objects.order_by('?')
    
    
    content = {
        'categorys': category,
        'title':'Главная',
        'posts':post,
    }
    return render(request, 'main/index.html',content)
    
    
def category_list(request, id):
    
    """ Реакция на нажатие категорий """
    
    category = Category.objects.all()
    post = Cars.objects.filter(category_id=id)
    content = {
        'categorys': category,
        'title':post[0].category,
        'posts':post,
    }
    return render(request, 'main/index.html',content)


def cars_detail(request, id):
    """ реакция на кнопку ПОДРОБНЕЕ """
    article = Cars.objects.get(id=id)
    content = {
        'title':article.title,
        'post':article,
    }
    return render(request, 'main/article.html',content)

def cars_history(request, id):
    history = Cars.objects.get(id=id)
    content = {
        'title':history.title,
        'history':history,
    }
    return render(request, 'main/history.html',content)


def UserLogin(request):
    """ антетификация пользователя """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт')
            return redirect('index')
    else:
        form = LoginForm()
    
    context = {
        'title':'Авторизация',
        'form':form
    }
    return render(request, 'main/login_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def Register(request):
    """ Регистрация пользователя """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = RegistrationForm()
    context = {
        'title':'Регистрация',
        'form':form
    }
    return render(request, 'main/register.html', context)


