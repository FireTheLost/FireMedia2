from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),
    path('blog-post/<uuid:pk>', views.BlogDetailView.as_view(), name='blog-post'),
]
