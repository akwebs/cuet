from django.db import models
from django.utils.text import slugify
from admin_section.models import basemodel
from tinymce.models import HTMLField
# Create your news models here.

class News_Category(basemodel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['title']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class News(basemodel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = HTMLField(null=True, blank=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(News_Category, on_delete=models.CASCADE, related_name='news_category')
    view_count = models.IntegerField(default=0)
    class Meta:
        ordering = ['-posted']
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title


