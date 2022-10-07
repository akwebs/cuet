from django.urls import path

from .views import *

app_name = 'news'

urlpatterns = [
    path('', news_view, name='news'),
    path('<slug:slug>/', news_details_view, name='news_detail'),
    path('category/<slug:slug>/', Categories_view, name='news_category'),
]
