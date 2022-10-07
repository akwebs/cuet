from django.shortcuts import render, get_object_or_404
from .models import News, News_Category

# Create your news views here.

def news_view(request):
    p = {
        'title' : 'News and Updates',
        'news': News.objects.all(),
        'categories': News_Category.objects.all(),
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'news/news.html', context)

def Categories_view(request, slug):
    p = {
        'title' : get_object_or_404(News_Category, slug=slug).title,
        'news': News.objects.filter(category=get_object_or_404(News_Category, slug=slug)),
        'categories': News_Category.objects.all(),
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'news/categories.html', context)

def news_details_view(request, slug):
    p = {
        'title' : get_object_or_404(News, slug=slug).title,
        'news': get_object_or_404(News, slug=slug),
        'categories': News_Category.objects.all(),
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'news/news_details.html', context)
