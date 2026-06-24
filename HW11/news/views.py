from django.shortcuts import get_object_or_404, render

from .models import Article, Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'news/home.html', {'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()
    return render(request, 'news/category_detail.html', {
        'category': category,
        'articles': articles,
    })


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {
        'article': article,
        'category': article.category,
    })