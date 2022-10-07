from django.db import models
from admin_section.models import basemodel
from study_material.models import syllabus
from tinymce.models import HTMLField
from django.utils.text import slugify
from all_imports.all_imports import *
# Create your models here.

class course_category(basemodel):
    category_name = models.CharField(max_length=100)
    category_status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.category_name
    class Meta:
        db_table = 'course_category'
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'

class course_subcategory(basemodel):
    subcategory_name = models.CharField(max_length=100)
    subcategory_status = models.BooleanField(default=True)
    category = models.ForeignKey(course_category, on_delete=models.CASCADE, related_name='subcategory')
    slug = models.SlugField(max_length=100, blank=True, null=True)
    unique_together = ('subcategory_name', 'category')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subcategory_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.subcategory_name + ' - ' + self.category.category_name
    class Meta:
        db_table = 'course_subcategory'
        verbose_name = 'Course Subcategory'
        verbose_name_plural = 'Course Subcategories'

class courses(basemodel):
    course_category = models.ForeignKey(course_category, on_delete=models.CASCADE, related_name='course_category', blank=True, null=True, verbose_name='Course Category')
    course_subcategory = models.ForeignKey(course_subcategory, on_delete=models.CASCADE, related_name='course_subcategory', verbose_name='Course Subcategory', blank=True, null=True)
    course_name = models.CharField(max_length=100, verbose_name='Course Name', unique=True, choices=SUBJECT_CHOICES)
    course_code = models.CharField(max_length=100, blank=True, null=True)
    course_description = HTMLField('Course Description', blank=True, null=True)
    text_booklets = models.IntegerField(default=0, blank=True, null=True)
    videos_lectures = models.IntegerField(default=0, blank=True, null=True)
    total_tests = models.IntegerField(default=0, blank=True, null=True)
    course_duration = models.IntegerField(default=0, blank=True, null=True)
    course_duration_unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='hours', blank=True, null=True)
    paper_pattern = HTMLField('Paper Pattern', blank=True, null=True)
    duration = models.IntegerField(default=0, blank=True, null=True)
    total_marks = models.IntegerField(default=0, blank=True, null=True)
    negative_marking = models.IntegerField(default=0, blank=True, null=True)
    syllabus = models.ForeignKey(syllabus, on_delete=models.CASCADE, related_name='syllabus', blank=True, null=True)
    course_status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.course_name
    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'