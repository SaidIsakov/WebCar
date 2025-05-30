from django.shortcuts import render,redirect
# Create your views here.
from .forms import PostAddForm
from .models import News

def news(request):
    
    news = News.objects.all()
    
    content = {
        'title':'Новости',
        'news':news,
    }
    return render(request, 'news/news.html', content)

def add_form(request):
    """Добавление новости от пользователя"""
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        if form.is_valid():
            # Сохраняем форму, что автоматически создает объект News
            form.save()
            # Редирект на страницу со списком новостей
            return redirect('news')  # 'news' - это name вашего URL в urls.py
    else:
        form = PostAddForm()
    
    context = {
        'title': 'Добавить новость',
        'form': form
    }
    return render(request, 'news/news_add_form.html', context)
