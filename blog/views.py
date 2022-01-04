from django.shortcuts import render
from django.views import generic

from .models import Blog, User


def index(request):
    user_count = User.objects.all().count()
    blog_count = Blog.objects.all().count()

    context = {
        'title': 'All Blog Posts',
        'user_count': user_count,
        'blog_count': blog_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
