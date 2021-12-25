from django.shortcuts import render

from applications.core.models import Post

from django.views.generic import ListView

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = 'created'
    context_object_name='blogs'
