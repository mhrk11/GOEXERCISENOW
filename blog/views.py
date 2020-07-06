from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy



class BlogListView(ListView):
    model=BlogPost
    template_name='home.html'
    context_object_name='blogs_list'
class BlogDetailView(DetailView):
    model=BlogPost
    template_name='post_detail.html'
class CreateBlog(CreateView):
    model=BlogPost
    template_name="new_post.html"
    fields=['title', 'author', 'body']

class UpdateBlog(UpdateView):
    model=BlogPost
    template_name='edit_post.html'
    fields=['title', 'body']

class DeleteBlog(DeleteView):
    model=BlogPost
    template_name='delete_post.html'
    success_url=reverse_lazy('home')








# Create your views here.
