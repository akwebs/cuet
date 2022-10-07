from django.contrib import admin
from .models import News, News_Category
# Register your models here.

@admin.register(News)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(News_Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']

