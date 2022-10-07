from django.shortcuts import render, get_object_or_404
from .models import blog, category

# Create your blog views here.

def Blog_view(request):
    blogs = blog.objects.all()
    categories = category.objects.all()
    p = {
        'title' : 'Blogs',
        'blogs': blogs,
        'categories': categories,
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'blog/blog.html', context)

def Categories_view(request, slug):
    p = {
        'title' : get_object_or_404(category, slug=slug).title,
        'blogs': blog.objects.filter(category=get_object_or_404(category, slug=slug)),
        'categories': category.objects.all(),
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'blog/categories.html', context)

def Blog_details_view(request, slug):
    p = {
        'title' : get_object_or_404(blog, slug=slug).title,
        'blog': get_object_or_404(blog, slug=slug),
        'categories': category.objects.all(),
        'comments': get_object_or_404(blog, slug=slug).comments.filter(active=True),
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'blog/blog_details.html', context)
