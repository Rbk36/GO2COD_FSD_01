from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from .models import Post

class Home(ListView):
    model=Post
    template_name='home.html'
    
class PostDetail(DetailView):
    model=Post
    template_name='post_detail.html'
    
class AddPost(CreateView):
    model=Post
    template_name='addpost.html'
    fields= '__all__'
