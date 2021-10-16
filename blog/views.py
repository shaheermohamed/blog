from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):  # new

    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):  # new

    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):  # new

    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
