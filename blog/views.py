from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'all_blogs'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['title'] = 'All Blogs'
        return context


class BlogDetailView(generic.DetailView):
    model = Blog

    def blog_detail_view(request, primary_key):
        blog = get_object_or_404(Blog, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={' blog': blog})

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Read Blog'
        return context
