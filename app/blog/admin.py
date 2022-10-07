from django.contrib import admin
from .models import blog, category, comment, blog_images
# Register your models here.

@admin.register(blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']

@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog', 'active')
    list_filter = ('active', )
    search_fields = ('name', 'email', 'body')
    ordering = ['created_at']

@admin.register(blog_images)
class BlogImagesAdmin(admin.ModelAdmin):
    list_display = ('image',)
    ordering = ['image']
    