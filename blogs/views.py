from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class Home(ListView):
    model=Post
    template_name='home.html'
    
class PostDetail(DetailView):
    model=Post
    template_name='post_detail.html'
