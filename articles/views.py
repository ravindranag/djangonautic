from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def articleListView(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/articleList.html', {'articles': articles})


def articleDetailView(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/articleDetail.html', {'article': article})