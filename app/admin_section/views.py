from django.shortcuts import render
from .models import *
from study_material.models import *
from course.models import *
# Create your views here.
def Home_view(request):
    s = sections.objects.all()
    c = carousel.objects.all()
    categories = course_category.objects.all()
    context = {
        'sections': s,
        'carousel': c,
        'categories': categories,
    }
    return render(request, 'home/index.html', context)

def About_view(request):
    p = {
        'title' : 'About CUET Sarthi',
        'content' : "",
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'home/about-cuet.html', context)

def Faq_view(request):
    f = faqs.objects.all()
    p = {
        'title' : 'FAQs',
        'content' : "",
        'faqs': f,
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'home/faqs.html', context)

def Syllabus_view(request):
    s = syllabus_sections.objects.all()
    p = {
        'title' : 'Syllabus',
        'content' : "",
        'syllabus': s,
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'home/syllabus.html', context)

def University_view(request):
    u = university_type.objects.all()
    p = {
        'title' : 'University',
        'content' : "",
        'university': u,
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'home/university.html', context)

def University_details_view(request, slug):
    u = university.objects.get(slug=slug)
    p = {
        'title' : u.name,
        'details' : u,
        'status': u.status,
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'home/university-details.html', context)

def Contact_view(request):
    p = {
        'title' : 'Contact Us',
        'content' : "",
    }
    context = {
        'content': p,
        'type': 'page',
    }
    return render(request, 'home/contact-us.html', context)