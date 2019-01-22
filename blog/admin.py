# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Student, Contact, Review, UserImage, Category, Course


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug": ("category_name",)}

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"course_slug": ("course_name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)


# Register your models here.
admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(UserImage)
