from django.urls import path
from .views import *
#NameError: name 'views' is not defined 
app_name = 'course'

urlpatterns = [
    path('', Courses_view, name='courses'),
    path('<slug:slug>/', Course_single_view, name='course'),
]
