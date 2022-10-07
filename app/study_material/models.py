from django.db import models
from admin_section.models import basemodel
from django.utils.text import slugify
from tinymce.models import HTMLField
from all_imports.all_imports import *


class study_material(basemodel):
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    code = models.CharField(max_length=100, blank=True, null=True)
    material_name = models.CharField(max_length=100, blank=True, null=True)
    pdf_file = models.FileField(upload_to='study_material', blank=True, null=True)
    material_description = HTMLField(null=True, blank=True)
    material_status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.material_name)
        super().save(*args, **kwargs)
    def pdfUrl(self):
        return self.pdf_file.url
    def __str__(self):
        return self.material_name
    class Meta:
        db_table = 'study_material'
        verbose_name = 'Study Material'
        verbose_name_plural = 'Study Materials'


class syllabus_sections(basemodel):
    section_name = models.CharField(max_length=100)
    section_status = models.BooleanField(default=True)
    def __str__(self):
        return self.section_name
    class Meta:
        db_table = 'syllabus_sections'
        verbose_name = 'Syllabus Section'
        verbose_name_plural = 'Syllabus Sections'


class syllabus(basemodel):
    syllabus_section = models.ForeignKey(syllabus_sections, on_delete=models.CASCADE, related_name='syllabus_sections', blank=True, null=True)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    code = models.CharField(max_length=100, blank=True, null=True)
    syllabus_name = models.CharField(max_length=100, blank=True, null=True)
    syllabus_file = models.FileField(upload_to='syllabus', blank=True, null=True)
    syllabus_description = HTMLField(null=True, blank=True)
    syllabus_status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.syllabus_name)
        super().save(*args, **kwargs)
    def pdfUrl(self):
        return self.syllabus_file.url
    def __str__(self):
        return self.syllabus_name
    class Meta:
        db_table = 'syllabus'
        verbose_name = 'Syllabus'
        verbose_name_plural = 'Syllabus'