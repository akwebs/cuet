from django.contrib import admin
from course.models import *
from .models import *
from team.models import *
from study_material.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(header)
class headerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'logo', 'logo_alt', 'cta_button_text')
    search_fields = ['title', 'logo', 'logo_alt', 'cta_button_text']
    list_filter = ['title', 'logo', 'logo_alt', 'cta_button_text']

# @admin.register(footer_widget)
# class footer_widgetAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('widget_name', 'widget_status', 'widget_content')
#     search_fields = ['widget_name', 'widget_status', 'widget_content']
#     list_filter = ['widget_status']

@admin.register(site_footer)
class site_footerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'logo', 'logo_alt' )
    search_fields = ['title', 'logo', 'logo_alt']
    list_filter = ['title', 'logo', 'logo_alt']

class menu_linksInline(admin.StackedInline):
    model = menu_links
    extra = 1


@admin.register(menus)
class menusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('menu_type', 'menu_name', 'menu_status')
    search_fields = ['menu_type', 'menu_name', 'menu_status']
    list_filter = ['menu_status']
    inlines = [menu_linksInline]


class sub_menu_linksInline(admin.StackedInline):
    model = sub_menu_links
    extra = 1

@admin.register(menu_links)
class menu_linksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('link_name','link_icon','link_url','link_status')
    search_fields = ['link_name','link_icon','link_url','link_status']
    list_filter = ['link_status']
    inlines = [sub_menu_linksInline]

@admin.register(sub_menu_links)
class sub_menu_linksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('link_name','link_icon','link_url','link_status')
    search_fields = ['link_name','link_icon','link_url','link_status']
    list_filter = ['link_status']

@admin.register(cta_buttons)
class cta_buttonsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('button_name', 'button_link', 'button_status')
    search_fields = ['button_name', 'button_link', 'button_status']
    list_filter = ['button_status']

@admin.register(carousel_images)
class carousel_imagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','image', 'image_alt', 'image_status')
    search_fields = ['title','image', 'image_alt', 'image_status']
    list_filter = ['image_status']

@admin.register(subtitles)
class subtitlesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('text', 'text_status')
    search_fields = ['text', 'text_status']
    list_filter = ['text_status']

@admin.register(carousel)
class carouselAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'background_image', 'background_image_alt', 'link', 'status') 
    search_fields = ['title', 'background_image', 'background_image_alt', 'link', 'status'] 
    list_filter = ['status']

@admin.register(hero)
class heroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'hero_text', 'hero_image')
    search_fields = ['title', 'hero_text', 'hero_image']

@admin.register(colors)
class colorsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('color_name', 'color_code', 'color_status')
    search_fields = ['color_name', 'color_code', 'color_status']
    list_filter = ['color_status']

# @admin.register(sections)
# class sectionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('sno', 'title', 'color', 'status')
#     search_fields = ['sno', 'title', 'color', 'status']
#     list_filter = ['status']

@admin.register(web_pages)
class web_pagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ['title', 'status']
    list_filter = ['status']

@admin.register(sections)
class sectionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'status','section_type')
    search_fields = ['title', 'status',]
    list_filter = ['status', 'section_type']

@admin.register(features)
class featuresAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ['title', 'status']
    list_filter = ['status']

@admin.register(faqs)
class faqsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ['title', 'status']
    list_filter = ['status']

@admin.register(contact_form)
class contact_formAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','email','phone','message')
    search_fields = ['name','email','phone','message']
    list_filter = ['name','email','phone']

@admin.register(testimonials)
class testimonialsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','designation','image','status')
    search_fields = ['name','designation','image','status']
    list_filter = ['status']

@admin.register(team_members)
class team_membersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('team_name','team_member_name','team_member_designation','team_member_image','team_member_status')
    search_fields = ['team_name','team_member_name','team_member_designation','team_member_image','team_member_status']
    list_filter = ['team_name', 'team_member_status']

@admin.register(study_material)
class study_materialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('subject','code','material_name','pdf_file','material_status')
    search_fields = ['subject','code','material_name','pdf_file','material_status']
    list_filter = ['subject','material_status']

class syllabusInline(admin.StackedInline):
    model = syllabus
    extra = 1


@admin.register(syllabus_sections)
class syllabus_sectionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('section_name','section_status')
    search_fields = ['section_name','section_status']
    list_filter = ['section_status']
    inlines = [syllabusInline]

@admin.register(syllabus)
class syllabusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('subject','code','syllabus_name','syllabus_file','syllabus_status')
    search_fields = ['subject','code','syllabus_name','syllabus_file','syllabus_status']
    list_filter = ['subject','syllabus_status']


#domains_language
@admin.register(domains_language)
class domains_languageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','status')
    search_fields = ['title','status']
    list_filter = ['status']

#programme_information
@admin.register(programme_information)
class programme_informationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','status')
    search_fields = ['title','status']
    list_filter = ['status']

@admin.register(university)
class universityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','status')
    search_fields = ['name','status']
    list_filter = ['status']
    filter_horizontal = ('programmes_information',)

@admin.register(university_type)
class university_typeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','status')
    search_fields = ['title','status']
    list_filter = ['status']
    filter_horizontal = ('universities',)