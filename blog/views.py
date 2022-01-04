import math

from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Blog, User


def index(request):
    users = User.objects.all().count()
    user_count = math.floor(math.log10(users)) if users > 10 else users - 1

    blogs = Blog.objects.all().count()
    blog_count = math.floor(math.log10(blogs)) if blogs > 10 else blogs - 1

    context = {
        'title': 'Blog Home',
        'user_count': user_count,
        'blog_count': blog_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'all_blogs'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['title'] = 'All Blogs'
        return context
