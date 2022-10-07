from django.urls import path
from .views import *
#NameError: name 'views' is not defined 
app_name = 'admin_section'

urlpatterns = [
    path('', Home_view, name='home'),
    path('about/', About_view, name='about'),
    path('faqs/', Faq_view, name='faqs'),
    path('syllabus/', Syllabus_view, name='syllabus'),
    path('universities/', University_view, name='university'),
    path('universities/<slug:slug>/', University_details_view, name='university_detail'),
    path('contact-us/', Contact_view, name='contact'),
]
