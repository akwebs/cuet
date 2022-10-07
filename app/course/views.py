from django.shortcuts import render
from .models import *
# Create your views here.
def Courses_view(request):
    categories = course_category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'course/index.html', context)

def Course_single_view(request, slug):
    course = courses.objects.filter(slug=slug).first()
    all_courses = courses.objects.exclude(slug=slug).all()
    context = {
        'course': course,
        'courses': all_courses,
    }
    return render(request, 'course/course.html', context)
