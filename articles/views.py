from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articleListView(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/articleList.html', {'articles': articles, 'title': 'Articles'})


def articleDetailView(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/articleDetail.html', {'article': article, 'title': article.title})

@login_required(login_url='accounts:login')
def createBlog(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create.html', {'title': 'Create Blog', 'form': form})