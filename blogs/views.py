from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from .models import Post
from .forms import PostForm

class Home(ListView):
    model=Post
    template_name='home.html'
    
class PostDetail(DetailView):
    model=Post
    template_name='post_detail.html'
    
class AddPost(CreateView):
    model=Post
    form_class=PostForm
    template_name='addpost.html'
    #fields= '__all__'
class EditPost(UpdateView):
    model=Post
    template_name='edit_post.html'
    fields=['title','body']

