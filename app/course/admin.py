from django.contrib import admin
from course.models import *
from import_export.admin import ImportExportModelAdmin

class subcategoryInline(admin.StackedInline):
    model = course_subcategory
    extra = 1

@admin.register(course_category)
class course_categoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['category_name','category_status']
    search_fields = ['category_name',]
    list_filter = ['category_status',]
    inlines = [subcategoryInline]

class coursesInline(admin.StackedInline):
    model = courses
    extra = 1

@admin.register(course_subcategory)
class course_subcategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'subcategory_status', 'category']
    search_fields = ['subcategory_name',]
    list_filter = ['subcategory_status',]
    inlines = [coursesInline]
    def name(self, obj):
        return str(obj.subcategory_name) + " (" + str(obj.category) + ")"

@admin.register(courses)
class coursesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('course_name','course_status')
    search_fields = ['course_name','course_status']
    list_filter = ['course_status']