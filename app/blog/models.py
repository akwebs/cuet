from django.db import models
from django.utils.text import slugify
from admin_section.models import basemodel
from tinymce.models import HTMLField
# Create your blog models here.

class category(basemodel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['title']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class blog_images(basemodel):
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True,)

    def __str__(self):
        return self.image.name

class blog(basemodel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ManyToManyField(blog_images, related_name='blog_images', blank=True)
    body = HTMLField(null=True, blank=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='blog_category')
    class Meta:
        ordering = ['-posted']
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.title

class comment(basemodel):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.blog)

