from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=['course_name','course_price','teacher']
admin.site.register(Course,CourseAdmin)
