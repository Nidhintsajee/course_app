    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Student(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    standard = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    review_url = models.SlugField(unique=True, default=uuid.uuid1)
    message = models.TextField()
    image = models.ImageField(upload_to ='review-user-image/')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject

class UserImage(models.Model):
    status = (('User','User'),('Admin','Admin'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='user-image/')
    position = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=status, default="User")

    def __str__(self):
        return self.author.username

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField()
    category_slug = models.SlugField()
    category_image = models.ImageField(upload_to ='category-image/')

    def __str__(self):
        return self.category_name

class Course(models.Model):
    author = models.ForeignKey(UserImage, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=200)
    course_price = models.CharField(max_length=200)
    course_description = RichTextField()
    course_image = models.ImageField(upload_to ='course-image/')
    course_slug = models.SlugField()



    def __str__(self):
        return self.course_name


