from django.contrib import admin
from django import forms

from blog.models import MyBlog, Tag

admin.site.register(MyBlog)
admin.site.register(Tag)

# Register your models here.
