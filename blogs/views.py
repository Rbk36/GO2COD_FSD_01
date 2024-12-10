from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        my_like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = my_like.total_likes()
        liked = False
        if self.request.user.is_authenticated and my_like.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    success_url = reverse_lazy('home')

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    success_url = reverse_lazy('home')

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in to like a post.")
        return redirect('home')

    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post detail', args=[str(pk)]))