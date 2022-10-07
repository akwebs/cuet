from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', Blog_view, name='blog'),
    path('<slug:slug>/', Blog_details_view, name='blog_detail'),
    path('category/<slug:slug>/', Categories_view, name='blog_category'),
]
