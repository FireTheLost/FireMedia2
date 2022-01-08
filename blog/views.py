import datetime
import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'all_blogs'
    paginate_by = 9

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-published')
        return ordering

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['title'] = 'All Blogs'
        return context


class BlogDetailView(generic.DetailView):
    model = Blog

    def blog_detail_view(request, primary_key):
        blog = get_object_or_404(Blog, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'blog': blog})

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Read Blog'
        return context


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'description', 'body', 'author']
    initial = {'id': uuid.uuid4, 'published': datetime.datetime.now(), 'visibility': 'Public'}

    def get_context_data(self, **kwargs):
        context = super(CreateBlog, self).get_context_data(**kwargs)
        context['title'] = 'Create Blog'
        return context
