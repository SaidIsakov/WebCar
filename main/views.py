from django.shortcuts import render
from .models import Category,Cars
# Create your views here.
def index(request):
    
    category = Category.objects.all()
    post = Cars.objects.all()
    
    content = {
        'categorys': category,
        'title':'Главная',
        'posts':post,
    }
    return render(request, 'main/index.html',content)
    
    
def category_list(request, id):
    category = Category.objects.all()
    post = Cars.objects.filter(category_id=id)
    content = {
        'categorys': category,
        'title':post[0].category,
        'posts':post,
    }
    return render(request, 'main/index.html',content)


def cars_detail(request, id):
    article = Cars.objects.get(id=id)
    content = {
        'title':article.title,
        'post':article,
    }
    return render(request, 'main/article.html',content)




