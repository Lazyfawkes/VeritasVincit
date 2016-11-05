from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from blog.models import MyBlog, Tag

class MyBlogListView(ListView):

    model = MyBlog

    def get_context_data(self, **kwargs):
        context = super(MyBlogListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context 
# Create your views here.
