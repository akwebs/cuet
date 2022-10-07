from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from django.utils.text import slugify
from all_imports.all_imports import *
#import reverse from django.urls
from django.urls import reverse
# Create your models here.
class basemodel(models.Model):
    created_by = models.ForeignKey('auth.User', related_name='%(class)s_created_by', on_delete=models.CASCADE, default=1)
    updated_by = models.ForeignKey('auth.User', related_name='%(class)s_updated_by', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class header(basemodel):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='header_images')
    logo_alt = models.CharField(max_length=100)
    cta_button_text = models.CharField(max_length=100)
    cta_button_icon = models.CharField(max_length=100)
    cta_button_link = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'site_header'
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'

# class footer_widget(basemodel):
#     widget_name = models.CharField(max_length=100)
#     widget_status = models.BooleanField(default=True)
#     widget_content = models.TextField(blank=True, null=True)
#     def __str__(self):
#         return self.widget_name
#     class Meta:
#         db_table = 'footer_widget'
#         verbose_name = 'Footer Widget'
#         verbose_name_plural = 'Footer Widgets'  

class site_footer(basemodel):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='footer_images', blank=True, null=True)
    logo_alt = models.CharField(max_length=100, blank=True, null=True)
    # footer_widget = models.ManyToManyField(footer_widget, blank=True, related_name='footer_widget', verbose_name='Footer Widget')
    copyright = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'footer'
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'

class menus(basemodel):
    menu_type = models.CharField(max_length=100, choices=(('main', 'Main'), ('footer', 'Footer')))
    menu_name = models.CharField(max_length=100)
    menu_status = models.BooleanField(default=True)
    def __str__(self):
        return self.menu_name
    class Meta:
        db_table = 'menus'
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

class menu_links(basemodel):
    menu = models.ForeignKey(menus, on_delete=models.CASCADE, related_name='menu_links', verbose_name='Menu', blank=True, null=True)
    link_name = models.CharField(max_length=100)
    link_icon = models.CharField(max_length=100, blank=True, null=True)
    link_url = models.CharField(max_length=100)
    link_status = models.BooleanField(default=True)
    sequence = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.link_name
    class Meta:
        db_table = 'menu_links'
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

class sub_menu_links(basemodel):
    link_parent = models.ForeignKey(menu_links, on_delete=models.CASCADE, related_name='sub_menu_links', verbose_name='Parent Link', blank=True, null=True)
    link_name = models.CharField(max_length=100)
    link_icon = models.CharField(max_length=100, blank=True, null=True)
    link_url = models.CharField(max_length=100)
    link_status = models.BooleanField(default=True)
    sequence = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.link_name
    class Meta:
        db_table = 'menu_links_sub'
        verbose_name = 'Menu Link Sub'
        verbose_name_plural = 'Menu Links Sub'


class cta_buttons(basemodel):
    header = models.ForeignKey(header, on_delete=models.CASCADE, related_name='cta_button_header', verbose_name='Header')
    button_name = models.CharField(max_length=100)
    button_icon = models.CharField(max_length=100)
    button_link = models.CharField(max_length=100)
    button_status = models.BooleanField(default=True)
    def __str__(self):
        return self.button_name
    class Meta:
        db_table = 'cta_buttons'
        verbose_name = 'Cta Button'
        verbose_name_plural = 'Cta Buttons'


class carousel_images(basemodel):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='carousel_images')
    image_alt = models.CharField(max_length=100)
    image_status = models.BooleanField(default=True)
    def __str__(self):
        return self.image_alt
    class Meta:
        db_table = 'carousel_images'
        verbose_name = 'Carousel Image'
        verbose_name_plural = 'Carousel Images'

class subtitles(basemodel):
    text = models.TextField()
    text_status = models.BooleanField(default=True)
    def __str__(self):
        return self.text
    class Meta:
        db_table = 'subtitles'
        verbose_name = 'Subtitle'
        verbose_name_plural = 'Subtitles'


class carousel(basemodel):
    title = models.CharField(max_length=100)
    subtitles = HTMLField(null=True,blank=True)
    cta_button = models.ForeignKey(cta_buttons, on_delete=models.CASCADE, related_name='cta_button_carousel', verbose_name='Cta Button', blank=True, null=True)
    image = models.ManyToManyField(carousel_images, blank=True, related_name='carousel_images', verbose_name='Carousel Image')
    background_image = models.ImageField(upload_to='carousel_images', blank=True, null=True)
    background_image_alt = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'carousel'
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'

class hero(basemodel):
    title = models.CharField(max_length=100)
    hero_text = models.ForeignKey(subtitles, on_delete=models.CASCADE, related_name='hero_text', verbose_name='Hero Text', blank=True, null=True)
    hero_image = models.ImageField(upload_to='hero_images')
    hero_image_alt = models.CharField(max_length=100)
    cta_button = models.ForeignKey(cta_buttons, on_delete=models.CASCADE, related_name='cta_button', verbose_name='Cta Button', blank=True, null=True)
    hero_content = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'hero'
        verbose_name = 'Hero'
        verbose_name_plural = 'Heros'

class colors(basemodel):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    color_status = models.BooleanField(default=True)
    def __str__(self):
        return self.color_name
    class Meta:
        db_table = 'colors'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

class testimonials(basemodel):
    name = models.CharField(max_length=100)
    text = models.TextField()
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials_images')
    image_alt = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'testimonials'
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class contact_form(basemodel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'contact_form'
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'


class faqs(basemodel):
    title = models.CharField(max_length=100)
    text = HTMLField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'faqs'
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

class features(basemodel):
    title = models.CharField(max_length=100)
    text = HTMLField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'features'
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'



class sections(basemodel):
    from course.models import courses
    section_type = models.CharField(max_length=100, choices=SECTION_CHOICES)
    title = models.CharField(max_length=100)
    text = HTMLField()
    courses = models.ManyToManyField(courses, blank=True, related_name='courses', verbose_name='Courses')
    testimonials = models.ManyToManyField(testimonials, blank=True, related_name='testimonials', verbose_name='Testimonials')
    faqs = models.ManyToManyField(faqs, blank=True, related_name='faqs', verbose_name='FAQs')
    features = models.ManyToManyField(features, blank=True, related_name='features', verbose_name='Features')
    image = models.ImageField(upload_to='about_us_images', blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'section'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

class web_pages(basemodel):
    title = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='web_pages_images', blank=True, null=True)
    background_image_alt = models.CharField(max_length=100, blank=True, null=True)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'web_pages'
        verbose_name = 'Web Page'
        verbose_name_plural = 'Web Pages'
        #define slug 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class domains_language(basemodel):
    title = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'domains_language'
        verbose_name = 'Domain Language'
        verbose_name_plural = 'Domain Languages'

class programme_information(basemodel):
    title = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    programme_course = models.CharField(max_length=100)
    domain_general_languages = models.ManyToManyField(domains_language, blank=True, related_name='domain_general_languages', verbose_name='Domain General Languages')
    eligibility = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'programme_information'
        verbose_name = 'Programme Information'
        verbose_name_plural = 'Programme Informations'

class university(basemodel):
    name = models.CharField(max_length=100)
    imp_note = HTMLField()
    programmes_information = models.ManyToManyField(programme_information, blank=True, related_name='programmes_information', verbose_name='Programmes Information')
    logo = models.ImageField(upload_to='university_images')
    image_alt = models.CharField(max_length=100)
    url = models.URLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'university'
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
    #define logoURL
    def logoURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url
    #define slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class university_type(basemodel):
    title = models.CharField(max_length=100)
    universities = models.ManyToManyField(university, blank=True, related_name='universities', verbose_name='Universities')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'university_type'
        verbose_name = 'University Type'
        verbose_name_plural = 'University Types'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)