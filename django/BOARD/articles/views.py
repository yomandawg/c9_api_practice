from django.shortcuts import render, redirect
from .models import Article


def index(request):
    # DB에 저장된 articles 불러와 보여줌
    articles = Article.objects.all().order_by('-id') # list 형태 뒤집어서
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
    
def new(request):
    return render(request, 'articles/new.html')
    
def create(request):
    # DB에 저장
    title = request.POST.get('title') # get parameters by POST method
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('detail', article.id) # redirect는 alias name + 인자

def detail(request, article_id):
    # id를 통해 해당하는 글을 찾아 보여줌
    article = Article.objects.get(id=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
    
def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_id):
    a = Article.objects.get(id=article_id)
    a.title = request.POST.get('title')
    a.content = request.POST.get('content')
    a.save()
    return redirect('detail', article_id)

def delete(request, article_id):
    a = Article.objects.get(id=article_id)
    a.delete()
    return redirect('index')