from django.shortcuts import render
# Create your views here.
from .models import News

def news(request):
    
    news = News.objects.all()
    
    content = {
        'title':'Новости',
        'news':news,
    }
    return render(request, 'news/news.html', content)