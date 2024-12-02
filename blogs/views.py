from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class Home(ListView):
    model=Post
    template_name='home.html'
    ordering=['-id']
    
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
    form_class=EditForm
    template_name='edit_post.html'
    #fields=['title','body']
class DeletePost(DeleteView):
     model=Post
     template_name='delete_post.html'
     success_url= reverse_lazy('home')
     

